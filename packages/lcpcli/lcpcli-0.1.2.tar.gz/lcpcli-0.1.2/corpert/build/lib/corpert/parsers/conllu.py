"""
Parser and writer for CONLLU-style data


ID: Word index, integer starting at 1 for each new sentence; may be a range for multiword tokens; may be a decimal number for empty nodes (decimal numbers can be lower than 1 but must be greater than 0).
FORM: Word form or punctuation symbol.
LEMMA: Lemma or stem of word form.
UPOS: Universal part-of-speech tag.
XPOS: Language-specific part-of-speech tag; underscore if not available.
FEATS: List of morphological features from the universal feature inventory or from a defined language-specific extension; underscore if not available.
HEAD: Head of the current word, which is either a value of ID or zero (0).
DEPREL: Universal dependency relation to the HEAD (root iff HEAD = 0) or a defined language-specific subtype of one.
DEPS: Enhanced dependency graph in the form of a list of head-deprel pairs.
MISC: Any other annotation.

"""

import re
import uuid

from inspect import isgenerator

from ._parser import Parser
from ..utils import CustomDict


FEATURES = [
    "id",
    "form",
    "lemma",
    "upos",
    "xpos",
    "feats",
    "head",
    "deprel",
    "deps",
    "misc",
]


class CONLLUParser(Parser):
    def __init__(self):
        super().__init__()
        self.word      = CustomDict()
        self.lemma     = CustomDict()
        self.ufeats    = CustomDict()
        self.jsonbMisc = CustomDict()
        self.xpos      = set()
        self.cur_idx   = 1
        self.cur_word  = 1
        self.cur_seg   = uuid.uuid4()
        self.left      = 1

        self.start_idx = re.compile(r"^\[\d+")
        self.end_idx   = re.compile(r"\d+\)$")
        self.text_id   = -1

    @property
    def right(self):
        return self.left + 1


    def parse_sentence(self, sentence_lines):
        """
        Take a list of ConLLU lines (comments + tokens) and output (sentence, new_doc | None)
        """
        new_doc = None
        current_sentence = {"meta": {}, "text": []}
        for line in sentence_lines:
            if re.match(r"# newdoc", line):
                new_doc = {"meta": {}, "sentences": {}, "id": (n_doc := n_doc+1)}
                if match := re.match(r"# newdoc id = (.+)", line):
                    new_doc["id"] = match[1]
                elif match := re.match(r"# newdoc ([^=]+) = (.+)", line):
                    new_doc["meta"][match[1]] = match[2]
            elif match := re.match(r"# sent_id = (.+)", line):
                current_sentence["id"] = match[1]
            elif match := re.match(r"#\s+([^=]+)\s+= (.+)", line):
                current_sentence["meta"][match[1]] = match[2]
            elif re.match(r"\d.*", line):
                line = line.split("\t")
                line = {k: v for k, v in zip(FEATURES, line)}
                current_sentence["text"].append(line)

        return (current_sentence, new_doc)


    def parse_generator(self, reader):
        sentence_lines = []
        while line := reader.readline():
            l = line.strip()
            if l:
                sentence_lines.append(line)
            else:
                # empty line: new sentence
                if sentence_lines:
                    yield self.parse_sentence(sentence_lines)
                sentence_lines = []

        if sentence_lines:
            yield self.parse_sentence(sentence_lines)


    def parse(self, content):
        """
        When iterator is True, yield ({id,meta,text},None|{id,meta}) -- content should have a readline method and 
        When iterator is False, return a writable string
        """

        conllu_parsed = {}
        current_document = {"meta": {}, "sentences": {}}
        current_sentences = {}

        n_doc = 0
        n_sent = 0

        sentences = [sent for sent in content.split("\n\n") if sent]

        for sent in sentences:

            sent_list = [line for line in sent.split("\n") if line]
            sentence, new_doc = self.parse_sentence(sent_list)

            if new_doc:
                if current_sentences:
                    current_document["sentences"] = current_sentences
                    conllu_parsed[current_document.pop("id",n_doc := n_doc+1)] = current_document
                current_document = new_doc
                current_sentences = {}

            current_sentences[sentence.pop("id", n_sent := n_sent+1)] = sentence

        if current_sentences:
            current_document["sentences"] = current_sentences
            conllu_parsed[current_document.pop("id",n_doc := n_doc+1)] = current_document

        return conllu_parsed


    def doc_meta(self, id, meta):
        """
        content is a dict {id,meta}
        """
        lines = []
        lines.append(f"# newdoc id = {id}")
        for key, value in meta.items():
            text = value.lstrip(" ").rstrip(" ") if value else None
            if not key or not text:
                continue
            lines.append(f"# newdoc {key} = {text}")
        return f"\n".join(lines)


    def combine(self, content):
        """
        content is a dict of filepaths and conllu data strings. combine them into one corpus and return as string?

        probably we have to add the filepaths to each sentence's sent-metadata
        """

        conllu_lines = []

        for doc_id, doc_content in content.items():
            conllu_lines.append(self.doc_meta(doc_id, doc_content.get("meta", {})))
            conllu_lines.append(self.write(doc_content.get("sentences", {})))

        return f"\n".join(conllu_lines)


    def write_sentence(self, sentence):
        lines = []
        sent_meta, sent_text = {}, []

        for item in sentence:
            if "meta" in item:
                sent_meta = sentence[item]
            elif "text" in item:
                sent_text = sentence[item]

        for k, v in sent_meta.items():
            lines.append("# {} = {}\n".format(k, v))

        if not sent_text:
            return lines

        lines.append(f"# text = {' '.join([token.get('form',' ') for token in sent_text])}\n")

        for n, item in enumerate(sent_text):
            # cols = [n+1, *item[1:]]
            # cols = [(str(i) if i else '_') for i in cols]
            # lines.append(f"\t".join(cols))
            lines.append(f"\t".join([item.get(f,'_') for f in FEATURES]))

        return lines


    def write_generator(self, generator):
        n_doc = 0
        n_sent = 0

        for sentence, doc in generator:
            lines = []
            # For now we don't support combine=False: yield new docs
            if doc:
                lines.append("# newdoc id = {}".format(doc.pop("id", n_doc := n_doc+1)))
                for k,v in doc.get("meta", {}).items():
                    lines.append("# newdoc {} = {}".format(k,v))
            lines.append("# sent_id = {}\n".format(sentence.pop("id", n_sent := n_sent+1)))
            lines += self.write_sentence(sentence)
            yield "".join(lines)

    def write(self, content, filename=None, combine=True, meta={}):
        """
        content is a dict of sentences: key is the id, value is {meta,text}
        """

        conllu_lines = []

        for sent_id, sent_data in content.items():

            if conllu_lines:
                conllu_lines.append(f"") # Add an empty line

            conllu_lines.append(f"# sent_id = {sent_id}\n")
            conllu_lines += self.write_sentence(sent_data)

        return f"\n".join(conllu_lines)
