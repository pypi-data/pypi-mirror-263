"""
Here we create an abstract base class from which all parsers should be derived.

Parsers require a .parse() and a .write() method at the least.

Note that .write() doesn't write to file, but returns a string that can be written to file!
"""
import abc
import json
import re

from ..utils import Sentence

class Parser(abc.ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @abc.abstractmethod
    def parse(self, content):
        """
        Turn a string of content into our abstract JSON format
        Format: {doc_id:{'meta':{},'sentences':{sent_id:{'meta':{},'text':{'id','form',...}}, ...}}}
        """
        pass

    @abc.abstractmethod
    def write(self, content, filename=None, combine=True, meta={}):
        """
        Create a writeable string from JSON data
        Content should use our abstract JSON format
        """
        pass

    @abc.abstractmethod
    def combine(self, content):
        """
        Combine a dictionary of {original_filepath: json_representation}
        """
        pass


    def compute_doc(self, content, first_sentence, last_sentence):
        """
        Return (doc_id,char_range,meta) for a given pair of first and last sentences
        """
        meta_obj = {}
        start_idx = re.search(self.start_idx, first_sentence)[0]
        end_idx   = re.search(self.end_idx, last_sentence)[0]
        char_range = f"{start_idx},{end_idx}"

        # meta_lines = [line for line in content.split("\n\n") if line.startswith("# text")]
        meta_lines = [line for line in content.split("\n") if line.startswith("# newdoc ")]
        for line in meta_lines:
            if " = " not in line:
                continue
            k, v = line.split(" = ")
            meta_obj[k[9:].strip()] = v.strip()

        # if "text_id" in meta_obj:
        if "id" in meta_obj:
            doc_id = meta_obj.pop("id")
        else:
            self.text_id += 1
            doc_id = self.text_id

        return doc_id, char_range, json.dumps(meta_obj)


    def generate_upload_files(self, content):
        """
        Return ([sentences], (doc_id,char_range,meta)) for a given document file
        """

        sentences = (sent for sent in content.split("\n\n") if sent)

        proc_sentences = []

        ncols = 0
        for sentence in sentences:
            lines = [x for x in sentence.split("\n") if x]

            sent = Sentence(lines, self)
            if sent._lines:
                sent.process()
                proc_sentences.append(sent)
                ncols = max([ncols, *[len(l) for l in sent.proc_lines]])

        for s in proc_sentences:
            for l in s.proc_lines:
                for _ in range(ncols - len(l)):
                    l.append("")

        if proc_sentences:
            doc = self.compute_doc(content, proc_sentences[0].proc_lines[0][6], proc_sentences[-1].proc_lines[-1][6])
            # self.compute_doc()
            return proc_sentences, doc
        else:
            return None, None