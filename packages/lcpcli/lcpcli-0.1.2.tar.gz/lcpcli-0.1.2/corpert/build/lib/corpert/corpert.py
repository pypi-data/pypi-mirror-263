import codecs
import csv
import json
import os

from datetime import date

from .parsers.conllu import CONLLUParser
from .parsers.vert import VERTParser
from .parsers.tei import TEIParser
from .parsers.json import JSONParser

from itertools import compress

# map between extensions and parsers
PARSERS = {
    "conllu": CONLLUParser,
    "vert": VERTParser,
    "xml": TEIParser,
    "tei": TEIParser,
    "json": JSONParser,
}

ERROR_MSG = """
Unrecognized input format.
Note: The converter currently supports the following formats:
.conllu, .xml (TEI), .json and .vert.
"""


class Corpert:
    @staticmethod
    def mask(llist, n=8):
        """
        computes a boolean mask to not write
        columns that are always empty.

        this is a simple heuristic which assumes that
        attrobutes that are always empty are not specified
        in the corpus template and therefore must not
        be written to the files to upload

        input is expected to be a list of
        of Sentence.proc_lines instances
        with a fixednumber of columns
        (not more or less dims)
        """
        mask = []
        for i in range(n):
            mask.append(any([x[i] for y in llist for x in y]))

        return mask

    def __init__(
        self,
        content,
        output=None,
        extension=None,
        filter=None,
        lua_filter=None,
        combine=True,
        mode=None
    ):
        """
        path (str): path or string of content
        combine (bool): create single output file?
        """
        self.output = os.path.abspath(output) if output else None
        self._output_format = None
        self.mode = mode
        if extension:
            self._output_format = extension
        elif self.output and self.output.endswith(
            (".json", ".xml", ".conllu", ".vert", ".tei")
        ):
            self._output_format = os.path.splitext(self.output)[-1]
        if self.output and not os.path.exists(self.output) and not combine:
            os.makedirs(self.output)
        self._filter = filter
        self._lua_filter = lua_filter
        self._lua = None
        self._input_files = []
        self._path = os.path.normpath(content)
        self._combine = combine
        self._on_disk = True
        if os.path.isfile(content):
            self._input_files.append(content)
        elif os.path.isdir(content):
            for root, dirs, files in os.walk(content):
                for file in files:
                    fullpath = os.path.join(root, file)
                    self._input_files.append(fullpath)
        elif isinstance(content, str):
            self._input_files.append(content)
            self._on_disk = False
        else:
            raise ValueError(ERROR_MSG)

    def __call__(self, *args, **kwargs):
        """
        Just allows us to do Corpert(**kwargs)()
        """
        return self.run(*args, **kwargs)

    def _detect_format_from_string(self, content):
        """
        todo: this, but accurately!
        """
        if "sent_id = " in content:
            return "conllu"
        elif "<xml" in content:
            return "xml"
        elif "<s sent_id" in content:
            return "vert"
        return "json"

    def _determine_format(self, filepath):
        """
        Deduce format from filepath, or from data string if need be
        """
        if os.path.isfile(filepath):
            if filepath.endswith(".conllu"):
                return "conllu"
            elif filepath.endswith(".vert"):
                return "vert"
            elif filepath.endswith(".xml"):
                return "xml"
            elif filepath.endswith(".json"):
                return "json"
        elif isinstance(filepath, str):
            return self._detect_format_from_string(filepath)
        raise ValueError(ERROR_MSG)

    def _write_json(self, combined):
        """
        Create JSON file(s) depending on combine setting
        """
        if self._combine:
            with open(self.output, "w") as fo:
                json.dump(combined, fo, indent=4, sort_keys=False)
        else:
            for path, data in combined.items():
                fixed_path = os.path.join(self.output, os.path.relpath(path))
                if not os.path.isdir(os.path.dirname(fixed_path)):
                    os.makedirs(os.path.dirname(fixed_path))
                with open(fixed_path, "w") as fo:
                    data = {path: data}
                    json.dump(data, fo, indent=4, sort_keys=False)

    def _write_to_file(self, filename, data):
        """
        Helper: write data to filename
        """
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        with open(filename, "w") as fo:
            fo.write(data)

    def _setup_filters(self):
        """
        If user wants to do lua/python filtering, we prepare things here
        """
        if self._lua_filter:
            import lupa
            from lupa import LuaRuntime

            self._lua = LuaRuntime(unpack_returned_tuples=True)
        elif self._filter:
            pass

    def _apply_lua_filter(self, content):
        """
        Run user's lua function on the JSON data for a file
        """
        with open(self._lua_filter, "r") as fo:
            script = fo.read()
        func = self._lua.eval(script)
        return func(content)

    def _apply_filter(self, content):
        """
        Run user's python function on the JSON data for a file
        """
        with open(self._filter, "r") as fo:
            script = fo.read()
        return exec(script, {}, {"content": content})

    def run(self):
        """
        The main routine: read in all input files and print/write them
        """
        combined = {}
        self._setup_filters()
        sents = []
        docs = []

        if self.mode == "upload":
            token_header = [
                "token_id",
                "form_id",
                "lemma_id",
                "upos",
                "xpos",
                "ufeat_id",
                "char_range",
                "segment_id"
            ]
            parser = CONLLUParser()
            sents = []

            for filepath in self._input_files:
                print(filepath)
                with open(filepath) as f:
                    content = f.read().strip()
                sent, doc = parser.generate_upload_files(content)
                if not sent:
                    continue
                sents += sent
                docs.append(doc)
                path = os.path.dirname(self._path)

            if len(sents[0].proc_lines[0]) > len(token_header):
                next_cell = str(sents[0].proc_lines[0][len(token_header)])
                if next_cell.startswith("[") and next_cell.endswith(")"):
                    token_header.append("frame_range")
                # import pdb; pdb.set_trace()
                if sents[0].parser.jsonbMisc._dictionary:
                    token_header.append("jsonb_id")
            mask = Corpert.mask([x.proc_lines for x in sents], len(token_header))

            with open(os.path.join(path, "token.csv"), "w") as f:
                csv_w = csv.writer(f, delimiter="\t", quotechar="\b")
                csv_w.writerow(list(compress(token_header, mask)))
                for sent in sents:
                    for line in sent.proc_lines:
                        csv_w.writerow(list(compress(line, mask)))

            if [s.deprel for s in sents if s.deprel]:
                with open(os.path.join(path, "deprel.csv"), "w") as f:
                    csv_w = csv.writer(f, delimiter="\t", quotechar="\b")
                    csv_w.writerow(["head", "dependent", "label", "left_anchor", "right_anchor"])
                    for sent in sents:
                        for line in sent.deprel:
                            csv_w.writerow(line)

            with open(os.path.join(path, "segment.csv"), "w") as f:
                csv_w = csv.writer(f, delimiter="\t", quotechar="\b")
                header = ["segment_id", "char_range"]
                if any(s.meta for s in sents):
                    header.append("meta")
                csv_w.writerow(header)
                for sent in sents:
                    row = [*sent.segment]
                    if "meta" in header:
                        row.append(json.dumps(sent.meta))
                    csv_w.writerow(row)

            with open(os.path.join(path, "fts_vector.csv"), "w") as f:
                csv_w = csv.writer(f, delimiter="\t", quotechar="\b")
                csv_w.writerow(["segment_id", "vector"])
                for sent in sents:
                    csv_w.writerow(sent.fts_vector)

            with open(os.path.join(path, "form.csv"), "w") as f:
                csv_w = csv.writer(f, delimiter="\t", quotechar="\b")
                csv_w.writerow(["form_id", "form"])
                for k, v in sents[0].parser.word._dictionary.items():
                    csv_w.writerow([v, k])

            with open(os.path.join(path, "lemma.csv"), "w") as f:
                csv_w = csv.writer(f, delimiter="\t", quotechar="\b")
                csv_w.writerow(["lemma_id", "lemma"])
                for k, v in sents[0].parser.lemma._dictionary.items():
                    csv_w.writerow([v, k])

            if sents[0].parser.ufeats._dictionary:
                with open(os.path.join(path, "ufeat.csv"), "w") as f:
                    csv_w = csv.writer(f, delimiter="\t", quotechar="\b")
                    csv_w.writerow(["ufeat_id", "ufeat"])
                    for k, v in sents[0].parser.ufeats._dictionary.items():
                        csv_w.writerow([v, k])

            if sents[0].parser.jsonbMisc._dictionary:
                with open(os.path.join(path, "jsonb.csv"), "w") as f:
                    csv_w = csv.writer(f, delimiter="\t", quotechar="\b")
                    csv_w.writerow(["jsonb_id", "jsonb"])
                    for k, v in sents[0].parser.jsonbMisc._dictionary.items():
                        csv_w.writerow([v, k])


            with open(os.path.join(path, "document.csv"), "w") as f:
                csv_w = csv.writer(f, delimiter="\t", quotechar="\b")
                csv_w.writerow(["document_id", "char_range", "meta"])
                for line in docs:
                    csv_w.writerow(line)

            json_file = os.path.join(path, "meta.json")
            if not os.path.isfile(json_file):
                json_obj = {
                    "meta": {
                        "name": next(reversed(path.split(os.path.sep))) or "Anonymous Project",
                        "author": "Anonymous",
                        "date": date.today().strftime("%Y-%m-%d"),
                        "version": 1,
                        "corpusDescription": ""
                    },
                    "firstClass": {
                        "document": "Document",
                        "segment": "Segment",
                        "token": "Token"
                    },
                    "layer": {
                        "Token": {
                            "abstract": False,
                            "layerType": "unit",
                            "anchoring": {
                                "location": False,
                                "stream": True,
                                "time": False
                            }
                        },
                        "Segment": {
                            "abstract": False,
                            "layerType": "span",
                            "contains": "Token"
                        },
                        "Document": {
                            "abstract": False,
                            "contains": "Segment",
                            "layerType": "span",
                        }
                    }
                }
                # Attributes of Token
                compressed_token_header = list(compress(token_header, mask))
                for n, attr in enumerate(compressed_token_header):
                    if attr in ("token_id", "segment_id", "char_range"):
                        continue
                    attr_no_id = attr[0:-3] if attr.endswith("_id") else attr
                    json_attr = json_obj["layer"]["Token"].get("attributes", {})
                    json_attr[attr_no_id] = {
                        "isGlobal": attr_no_id in ('upos', 'ufeat'),
                        "type": "text" if attr.endswith("_id") else "categorical",
                        "nullable": not (attr == "lemma_id")
                    }
                    if json_attr[attr_no_id]["type"] == "categorical" and not json_attr[attr_no_id]["isGlobal"]:
                        values = set()
                        for sent in sents:
                            for line in sent.proc_lines:
                                values.add(list(compress(line, mask))[n])
                        json_attr[attr_no_id]["values"] = list(values)
                    json_obj["layer"]["Token"]["attributes"] = json_attr
                # Meta attributes of Document
                meta_docs = set()
                for line in docs:
                    meta_obj = json.loads(line[2])
                    if not meta_obj:
                        continue
                    meta_docs = meta_docs.union(set(k for k in meta_obj.keys()))
                json_obj["layer"]["Document"]["attributes"] = {
                    "meta": {
                        k: {
                        "type": "text",
                        "nullable": True
                        } for k in meta_docs
                    }
                }
                json_str = json.dumps(json_obj,indent=4)
                open(json_file, "w").write(json_str)
                print(f"\n{json_str}\n")
                print(f"A default meta.json file with the structure above was automatically generated at '{json_file}' for the current corpus.")
                print(f"Please review it and make any changes as needed in a text editor.")
                print(f"Once the file contains the proper information, press any key to proceed.")
                input()
            else:
                print(f"outfiles written to '{path}'.")

        else:
            format = (self._output_format or "").lstrip(".")

            for filepath in self._input_files:
                print("input file", filepath)
                if os.path.isfile(filepath):
                    parser = PARSERS[self._determine_format(filepath)]()
                else:
                    parser = self._detect_format_from_string(filepath)

                reader = parser.parse_generator(codecs.open(filepath,"r","utf8"))
                for sentence in parser.write_generator(reader):
                    print("writing", sentence)

                continue
                if self._on_disk:
                    with codecs.open(filepath, "r", "utf8") as fo:
                        content = fo.read()
                else:
                    content = filepath

                understood = parser.parse(content)
                if self._filter:
                    understood = self._apply_filter(understood)
                if self._lua_filter:
                    understood = self._apply_lua_filter(understood)

                if len(understood) == 1:
                    combined[filepath] = next(v for _,v in understood.items())
                else:
                # if 'documents' in understood:
                    for doc, v in understood.items():
                        subfilepath = os.path.join(filepath, f"{doc}.{format}")
                        combined[subfilepath] = v
                # else:
                #     combined[filepath] = understood

            return

            if not self.output:
                print(json.dumps(combined, indent=4, sort_keys=False))
                return combined
            elif self._output_format.endswith("json"):
                self._write_json(combined)
                return
            else:
                parser = PARSERS[format]()
                if not self._combine:
                    # print("combined", combined)
                    for path, data in combined.items():
                        # text_id = os.path.splitext(os.path.basename(path))[0]
                        meta = {"id": path, **data.get("meta",{})}
                        formatted = parser.write(data.get("sentences",{}), path, combine=False, meta=meta)
                        # fixed_path = os.path.join(self.output, os.path.relpath(path))
                        fixed_path = os.path.join(self.output, os.path.basename(path))
                        # print(f"writing {len(formatted)} chars to {fixed_path}")
                        self._write_to_file(fixed_path, formatted)
                    return
                else:
                    if len(combined) == 1:
                        path, data = combined.popitem()
                        meta = {"id": path, **data.get("meta",{})}
                        formatted = parser.write(data.get("sentences", {}), path, combine=False, meta=meta)
                    else:
                        formatted = parser.combine(combined)
                    self._write_to_file(self.output, formatted)
                    return

            raise ValueError(ERROR_MSG.replace("input", "output"))



if __name__ == "__main__":
    """
    When the user calls the script directly in command line, this is what we do
    """
    from .cli import _parse_cmd_line

    kwargs = _parse_cmd_line()
    Corpert(**kwargs).run()
