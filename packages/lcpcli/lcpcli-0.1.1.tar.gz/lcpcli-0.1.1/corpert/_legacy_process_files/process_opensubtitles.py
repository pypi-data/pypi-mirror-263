import csv
import uuid
import lzma
import re

from datetime import timedelta
from timeit import default_timer as timer


green = "\033[92m"
end = "\033[0m"


### DATA & WRITE FILES

PREFIX    = "/srv/data/jonathan/open_subtitles_en/"

DEPREL_F1  = PREFIX + "deprel1.csv"
DEPREL_F2  = PREFIX + "deprel2.csv"
LINES_F1   = PREFIX + "lines1.csv"
LINES_F2   = PREFIX + "lines2.csv"
SEGMENT_F1 = PREFIX + "segment1.csv"
SEGMENT_F2 = PREFIX + "segment2.csv"
FTS_F1     = PREFIX + "fts_vector1.csv"
FTS_F2     = PREFIX + "fts_vector2.csv"
DOC_F      = PREFIX + "document.csv"
WORD_F     = PREFIX + "word.csv"
LEMMA_F    = PREFIX + "lemma.csv"
UFEAT_F    = PREFIX + "ufeat.csv"
XPOS_F     = PREFIX + "xpos.csv"

DATA_F    = "/home/jonathan/TEMP_DIR/Projects/LCP/corpora/OpenSubtitles/OpenSubtitles_en.stanza.tsv.xz"



def user_confirmation(message):
    conf = input(message)

    if conf.lower() != "y":
        print("aborting.")
        exit(1)


class MyDict:
    def __init__(self, is_ufeat=False):
        self._dictionary = {}
        self._max        = 1
        self._is_ufeat   = is_ufeat

    def __str__(self):
        return str(self._dictionary)

    def update(self, value):
        if self._is_ufeat and value == '{"_"}':
            return

        if value and value not in self._dictionary:
            self._dictionary[value] = self._max
            self._max += 1

    def get(self, value):
        return self._dictionary.get(value, None)


class GlobalState:
    word      = MyDict()
    lemma     = MyDict()
    ufeats    = MyDict(is_ufeat=True)
    xpos      = set()
    docs      = {}
    in_id_doc = False
    no_id     = 0
    cur_idx   = 1
    cur_word  = 1
    cur_seg   = uuid.uuid4()
    left      = 1
    right     = 2


# TODO: not in use yet...
# class TokenData:
#     def __init__(self    , word_id, form_id,
#                  lemma_id, upos   , xpos   , ufeats,
#                  s_idx   , e_idx  , seg_id , deprel):
#         self.word_id  = word_id
#         self.form_id  = form_id
#         self.lemma_id = lemma_id
#         self.upos     = upos
#         self.xpos     = xpos
#         self.ufeats   = ufeats
#         self.s_idx    = s_idx
#         self.e_idx    = e_idx
#         self.seg_id   = seg_id
#         self.deprel   = deprel


class Sentence:
    _id_pat    = re.compile(r"^# id=(\d+)?")
    _start_pat = re.compile(r"(?<=S=).+$")
    _end_pat   = re.compile(r"(?<=E=).+$")

    @staticmethod
    def underscore2null(value):
        if value == "_":
            return None
        else:
            return value

    @staticmethod
    def valid_lines(lines):
        ret_lines = []
        for line in lines:
            if line.startswith("#"):
                continue
            split_l = line.split("\t")
            if "-" in split_l[0]:
                continue
            ret_lines.append(split_l)

        return ret_lines

    @staticmethod
    def jsonify_ufeats(string):
        # change angular brackets to parens
        string = string.replace("[", "(").replace("]", ")")
        # put alternatves inside JSON-array
        string = re.sub(r"(\w+,\s*\w+)", r"[\1]", string)
        # convert pipes -separator to comma
        string = string.replace("|", ",")
        # converts equal to colon
        string = string.replace("=", ":")
        # surround literals with double quotes
        string = re.sub(r"([\w()]+)", r'"\1"', string)

        return "{" + string + "}"

    @staticmethod
    def _append(lst, elem):
        """custom append function

           in contrast to the built-in method, this function returns
           the augmented list - useful for recursive calls
        """
        lst.append(elem)

        return lst

    @staticmethod
    def _traverse(hierarchy, graph, ids):
        """traverse flat list & build hierarchical structure

           the flat structure is a parent: children dict
        """
        for id in ids:
            hierarchy[id] = Sentence._traverse({}, graph, graph[id])

        return hierarchy

    @staticmethod
    def _ord_keys(dic, key_list):
        """traverse tree structure & build flat list

        """
        for el, vals in dic.items():
            Sentence._ord_keys(vals, Sentence._append(key_list, el))

        return key_list

    @staticmethod
    def _esc(string):
        return string.replace("'", "''").replace("\\", "\\\\")
        # return string

    def __init__(self, lines, glob):
        self._lines     = self.valid_lines(lines)
        self._headers   = [x for x in lines if x.startswith("#")]
        self._id        = None
        self._start     = None
        self._end       = None
        self.glob       = glob
        self.proc_lines = []
        self.segment    = []
        self.deprel     = []
        self.fts_vector = []

    def _scan_headers(self):
        for line in self._headers:
            id = re.search(self._id_pat, line)
            if id:
                if id[1]:
                    self._id = id[1]
                    if not self.glob.in_id_doc:
                        self.glob.in_id_doc = True
                else:
                    if self.glob.in_id_doc:
                        self.glob.no_id -= 1
                        self.glob.in_id_doc = False
                    self._id = str(self.glob.no_id)
            start = re.search(self._start_pat, line)
            if start:
                self._start = start[0]
            end = re.search(self._end_pat, line)
            if end:
                self._end = end[0]

    def _tree_ins_order(self):
        """ put list in hierarchical order for inserting

            1. create dictionary structure (recursively)
            2. flatten keys recursively into list
            3. go over original list and append to
               return list according to flattened keys
        """
        # index 2 = id, index 4 = head ATTENTION: adjust, if this changes!
        id_par   = [(x[0], x[6]) for x in self._lines]
        ret_list = []

        # get root and check iff one
        root = [id for (id, parent) in id_par if parent == "0"]
        if len(root) != 1:
            raise Exception("root error")

        # flat parent:children mapping initialization
        graph = {id: set() for (id, parent) in id_par}

        # flat parent:children mapping building
        for (id, parent) in id_par:
            if parent != "0":
                graph[parent].add(id)

        # sorting in reverse, since inserting is done by shifting to the right
        graph_sort = {k: sorted(v, key=lambda x: int(x), reverse=True) for k, v in graph.items()}

        # build hierarchical structure
        hier_ids = self._traverse({}, graph,  root)

        # flatten keys into ordered list
        flat_keys = self._ord_keys(hier_ids, [])

        # re-order original rows for returning
        for i in flat_keys:
            for pair in id_par:
                if pair[0] == i:
                    ret_list.append(pair)
                    continue

        return ret_list

    def _process_tree(self, ins, token_dict, tok_par_dict):
        sent       = []
        fts_str    = ""
        root, rest = ins[0], ins[1:]
        tree       = NestedSetTreeStructure(root[0], self.glob.left, self.glob.right)
        for elem in rest:
            tree.add_node(*elem)

        # update globals
        self.glob.left = max([x[1] for x in tree.nodes.values()]) + 1
        self.glob.right = self.glob.left + 1

        # look-up running indices and flatten into list
        for k, v in tree.nodes.items():
            token_id = token_dict[k][0]
            deprel = token_dict[k][1]
            head_id = token_dict[tok_par_dict[k]][0] if tok_par_dict[k] else None
            sent.append((head_id, token_id, deprel, *v))

        self.deprel += sent

        # 4 = label_out (what am I?), 5 = labels_in (what do I encompass?)
        tok_id2sent_idx = {v[0]: k for k, v in token_dict.items()}
        for elem in sent:
            fts_str += f" '4{elem[2]}':{tok_id2sent_idx[elem[1]]}"
            fts_str += f" '5{elem[2]}':{tok_id2sent_idx[elem[1]]}"

        return fts_str

    def _process_lines(self):
        # set up local variables
        token_dict   = {}
        tok_par_dict = {}
        fts_str      = ""
        start_char   = self.glob.cur_idx
        end_char     = None

        for line in self._lines:
            w_id, word, lemma, upos, xpos, ufeats, p_id, deprel, _, _ = line

            assert w_id
            assert word

            lemma, upos, xpos, ufeats, p_id, deprel = [self.underscore2null(x) for x in [lemma, upos, xpos, ufeats, p_id, deprel]]

            l_word   = len(word)
            end_char = self.glob.cur_idx + l_word
            ufeats   = self.jsonify_ufeats(ufeats)

            # update global dicts
            self.glob.word.update(word)
            self.glob.lemma.update(lemma)
            self.glob.ufeats.update(ufeats)
            self.glob.xpos.update(xpos)

            # dictionary holding all info for 1 token
            # TODO: this is not right 100% since w_id not always unique...
            # word_id, form_fk, lemma_fk, upos, xpos, ufeat_fk, char_range, seg_fk
            token_dict[w_id] = [
                self.glob.cur_word,
                self.glob.word.get(word),
                self.glob.lemma.get(lemma),
                upos,
                xpos,
                self.glob.ufeats.get(ufeats),
                (self.glob.cur_idx, end_char),
                self.glob.cur_seg,
                deprel
            ]

            fts_str += f" '1{self._esc(word)}':{w_id} '2{self._esc(lemma)}':{w_id} '6{xpos}':{w_id} '3{upos}':{w_id}"

            # update global word id and index
            self.glob.cur_idx  += l_word
            self.glob.cur_word += 1

            tok_par_dict[w_id] = p_id if p_id != "0" else None

        # create line entry for writing
        self.proc_lines = [
            line[:6]                         + \
            [f"[{line[6][0]},{line[6][1]})"] + \
            [line[7]] for line in token_dict.values()
        ]

        # build tree (if possible)
        try:
            ins = self._tree_ins_order()
            fts = self._process_tree(ins, {k: (v[0], v[-1]) for k, v in token_dict.items()}, tok_par_dict)
        except:
            fts = ""

        # create segment entry for writing
        self.segment = [
            self.glob.cur_seg,
            f"[{start_char},{end_char})",
            self._start,
            self._end,
            self._id
        ]

        self.fts_vector = [
            self.glob.cur_seg,
            f"{fts_str}{fts}"
        ]


        # set new segment id
        self.glob.cur_seg = uuid.uuid4()


        # create doc entry for writing
        if self._id:
            if self._id in self.glob.docs:
                self.glob.docs[self._id][1] = end_char
            else:
                self.glob.docs[self._id] = [start_char, end_char]


    def process(self):
        self._scan_headers()
        self._process_lines()



class NestedSetTreeStructure:
    """
    Represents a tree structure with the nested set approach.
    """

    def __init__(self, key, left, right):
        self.nodes = {}
        if not right - left == 1:
            raise Exception("invalid anchors for initialization")
        self.nodes[key] = [left, right]

    def __str__(self):
        """
        Returns a pretty-print version of the tree.
        """
        lines     = []
        last_left = 0
        indent    = -1
        for key, node in sorted(self.nodes.items(), key=lambda item: item[1]):
            if node[0] - last_left == 1:
                indent += 1
            elif node[0] - last_left > 2:
                indent -= 1
            lines.append("{}{}  [{},{}]".format(
                (indent-1)*"│  " + ("" if node[0] == 1 else "├─╴"),
                key,
                node[0],
                node[1]
            ))
            last_left = node[0]
        return '\n'.join(lines)

    def shift_anchors(self, parent_left):
        """
        Makes space in the tree by incrementing all nodes to the right by 2.
        """
        for key, node in self.nodes.items():
            if node[0] > parent_left:
                self.nodes[key][0] += 2
            if node[1] > parent_left:
                self.nodes[key][1] += 2

    def add_node(self, key, parent):
        """
        Adds a node giving the id of the parent or None for the root node.
        """
        if parent is None:
            if len(self.nodes):
                raise Exception("there can only be one root node")
            else:
                self.nodes[key] = [1, 2]
        else:
            if parent in self.nodes:
                parent_node = self.nodes[parent]
            else:
                raise Exception("key does not exist: {}".format(parent))
            self.shift_anchors(parent_node[0])
            self.nodes[key] = [parent_node[0]+1, parent_node[0]+2]


def yield_block(xzf):
    block = []
    with lzma.open(xzf, "rt") as f:
        for line in f:
            if line != "\n":
                block.append(line)
            else:
                yield block
                block = []

        if block:
            yield block


def main():
    globs = GlobalState()
    t_start = timer()

    with open(DEPREL_F1, "w")  as dep_f1, \
         open(DEPREL_F2, "w")  as dep_f2, \
         open(LINES_F1, "w")   as lin_f1, \
         open(LINES_F2, "w")   as lin_f2, \
         open(SEGMENT_F1, "w") as seg_f1, \
         open(SEGMENT_F2, "w") as seg_f2, \
         open(FTS_F1, "w")     as fts_f1, \
         open(FTS_F2, "w")     as fts_f2, \
         open(DOC_F, "w")      as doc_f:
        dep_w1 = csv.writer(dep_f1, delimiter="\t", quotechar="\b")
        dep_w2 = csv.writer(dep_f2, delimiter="\t", quotechar="\b")
        lin_w1 = csv.writer(lin_f1, delimiter="\t", quotechar="\b")
        lin_w2 = csv.writer(lin_f2, delimiter="\t", quotechar="\b")
        seg_w1 = csv.writer(seg_f1, delimiter="\t", quotechar="\b")
        seg_w2 = csv.writer(seg_f2, delimiter="\t", quotechar="\b")
        fts_w1 = csv.writer(fts_f1, delimiter="\t", quotechar="\b")
        fts_w2 = csv.writer(fts_f2, delimiter="\t", quotechar="\b")
        doc_w = csv.writer(doc_f, delimiter="\t", quotechar="\b")
        for i, block in enumerate(yield_block(DATA_F)):
            dep_w = dep_w1 if i < 250_000_000 else dep_w2
            lin_w = lin_w1 if i < 250_000_000 else lin_w2
            seg_w = seg_w1 if i < 250_000_000 else seg_w2
            fts_w = fts_w1 if i < 250_000_000 else fts_w2
            sent = Sentence(block, globs)
            sent.process()

            # if not sent.deprel:
            #     import pdb; pdb.set_trace()

            for elem in sent.proc_lines:
                lin_w.writerow(elem)
            for elem in sent.deprel:
                dep_w.writerow(elem)
            seg_w.writerow(sent.segment)
            fts_w.writerow(sent.fts_vector)

            if i % 10_000_000 == 0 and i != 0:
                t_count = timer()
                t = timedelta(seconds=t_count-t_start)
                print(f"Processed {i:,} segments. time elapsed: {t}")

                if i == 250_000_000:
                    print("closing files")
                    dep_f1.close()
                    lin_f1.close()
                    seg_f1.close()
                    fts_f1.close()
                    input("push 1s to DB, then continue by pressing any key")

        for k, v in sent.glob.docs.items():
            doc_w.writerow([k, f"[{v[0]},{v[1]})"])

    print("writing dictionaries...")
    with open(WORD_F, "w") as wor_f,  \
         open(LEMMA_F, "w") as lem_f, \
         open(UFEAT_F, "w") as ufe_f:
        wor_w = csv.writer(wor_f, delimiter="\t")
        lem_w = csv.writer(lem_f, delimiter="\t")
        ufe_w = csv.writer(ufe_f, delimiter="\t")

        for k, v in globs.word._dictionary.items():
            wor_w.writerow([v, k])
        for k, v in globs.lemma._dictionary.items():
            lem_w.writerow([v, k])
        for k, v in globs.ufeats._dictionary.items():
            ufe_w.writerow([v, k])



if __name__ == "__main__":
    data_file_msg = f"processing file  '{green}{DATA_F}{end}'"
    write_dir_msg = f"writing to dir   '{green}{PREFIX}{end}'"
    print()
    user_confirmation(
        data_file_msg + \
        "\n"          + \
        write_dir_msg + \
        "\n\ncontinue (y/Y)? "
    )

    main()

