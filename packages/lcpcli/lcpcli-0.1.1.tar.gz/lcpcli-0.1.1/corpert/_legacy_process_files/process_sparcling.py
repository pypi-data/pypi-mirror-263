import csv
import lzma
import psycopg2
import uuid

from datetime import timedelta
from timeit import default_timer as timer


green = "\033[92m"
end = "\033[0m"


### DATA & WRITE FILES

PREFIX    = "proc_files2/"

DEPREL_F  = PREFIX + "deprel.csv"
LINES_F   = PREFIX + "lines.csv"
SEGMENT_F = PREFIX + "segment.csv"
WORD_F    = PREFIX + "word.csv"
LEMMA_F   = PREFIX + "lemma.csv"
UFEAT_F   = PREFIX + "ufeat.csv"
XPOS_F    = PREFIX + "xpos.csv"

DATA_F    = [
                # ("FEP9/token.de.tsv.xz", "german"),
                # ("FEP9/token.en.tsv.xz", "english"),
                ("FEP9/token.fr.tsv.xz", "french")
            ]



def user_confirmation(message):
    conf = input(message)

    if conf.lower() != "y":
        print("aborting.")
        exit()


def yield_block(xzf):
    block = []
    with lzma.open(xzf, "rt") as f:
        for line in f:
            if line != "\n" and not line.startswith("#"):
                block.append(line.strip())
            else:
                # only used for excluding first header line
                if block:
                    yield block
                    block = []
                else:
                    continue

        if block:
            yield block


# def get_meta_dicts(meta_text_file):
#     """
#     function that builds the dictionaries
#     used as lookups for text IDs
#     """
#     line_doc, line_chp, line_trn,  = {}, {}, {}

#     lines = [l.split("\t").strip() for l in [x for x in yield_line(meta_text_file)]]

#     for line in lines:
#         num_line, key_val = line[0], {x.split("=")[0]: x.split("=")[1] for x in line[1].split("|")}
#         line_doc[num_line] = key_val.pop("Session")
#         line_chp[num_line] = key_val.pop("Chapter")
#         line_trn[num_line] = key_val

#     return line_doc, line_chp, line_trn


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

        if not value in self._dictionary:
            self._dictionary[value] = self._max
            self._max += 1

    def get(self, value):
        return self._dictionary.get(value, None)


class GlobalState:
    word      = MyDict()
    lemma     = MyDict()
    docs      = {}
    cur_idx   = 1
    cur_seg   = uuid.uuid4()
    left      = 1
    right     = 2


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


class Sentence:
    @staticmethod
    def split_lines(lines):
        ret_lines = []
        for line in lines:
            split_l = line.split("\t")
            ret_lines.append(split_l)

        return ret_lines

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

    def __init__(self, lines, glob, lang):
        self._lines     = self.split_lines(lines)
        self.glob       = glob
        self.proc_lines = []
        self.segment    = []
        self.deprel     = []
        self.lang       = lang

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
        hier_ids = self._traverse({}, graph_sort,  root)

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
            deprel   = token_dict[k][1]
            head_id  = token_dict[tok_par_dict[k]][0] if tok_par_dict[k] else None
            self.deprel.append((head_id, token_id, deprel, *v))

    def _process_lines(self):
        # set up local variables
        token_dict   = {}
        tok_par_dict = {}
        start_char   = self.glob.cur_idx
        end_char     = None

        for line in self._lines:
            w_id,         \
            word,         \
            lemma,        \
            upos,         \
            xpos,         \
            _,            \
            p_id,         \
            deprel,       \
            _,            \
            space_after,  \
            pacoco_tokid, \
            pacoco_senid, \
            pacoco_txtid = line

            l_word   = len(word)
            end_char = self.glob.cur_idx + l_word

            # update global dicts
            self.glob.word.update(word)
            self.glob.lemma.update(lemma)

            # dictionary holding all info for 1 token
            # TODO: this is not right 100% since w_id not always unique...
            # word_id, form_fk, lemma_fk, upos, xpos, ufeat_fk, char_range, seg_fk
            token_dict[w_id] = [
                pacoco_tokid,
                self.glob.word.get(word),
                self.glob.lemma.get(lemma),
                upos,
                xpos,
                (self.glob.cur_idx, end_char),
                self.glob.cur_seg,
                deprel
            ]

            # update global word id and index
            if space_after != "_":
                self.glob.cur_idx += l_word
            else:
                self.glob.cur_idx += l_word + 1

            tok_par_dict[w_id] = p_id if p_id != "0" else None

        # create line entry for writing
        self.proc_lines = [
            line[:5]                         + \
            [f"[{line[5][0]},{line[5][1]})"] + \
            [line[6]] for line in token_dict.values()
        ]

        # build tree (if possible)
        try:
            ins = self._tree_ins_order()
            self._process_tree(ins, {k: (v[0], v[-1]) for k, v in token_dict.items()}, tok_par_dict)
        except:
            pass

        # create segment entry for writing
        self.segment = [
            self.glob.cur_seg,
            pacoco_senid,
            pacoco_txtid,
            f"[{start_char},{end_char})"
        ]
        # set new segment id
        self.glob.cur_seg = uuid.uuid4()


    def process(self):
        self._process_lines()


def main():
    globs = GlobalState()
    t_start = timer()

    with open(DEPREL_F, "w") as dep_f,  \
         open(LINES_F, "w") as lin_f,   \
         open(SEGMENT_F, "w") as seg_f:
        dep_w = csv.writer(dep_f, delimiter="\t")
        lin_w = csv.writer(lin_f, delimiter="\t")
        seg_w = csv.writer(seg_f, delimiter="\t")
        for f, lang in DATA_F:
            for i, block in enumerate(yield_block(f)):
                sent = Sentence(block, globs, lang)
                sent.process()

                # if not sent.deprel:
                #     import pdb; pdb.set_trace()

                for elem in sent.proc_lines:
                    lin_w.writerow(elem)
                for elem in sent.deprel:
                    dep_w.writerow(elem)
                seg_w.writerow(sent.segment)

                if i % 100_000 == 0 and i != 0:
                    t_count = timer()
                    t = timedelta(seconds=t_count-t_start)
                    print(f"Processed {i:,} segments. time elapsed: {t}")

                # if i == 1_000_000:
                #     break


    print("writing dictionaries...")
    with open(WORD_F, "w") as wor_f,  \
         open(LEMMA_F, "w") as lem_f:
        wor_w = csv.writer(wor_f, delimiter="\t")
        lem_w = csv.writer(lem_f, delimiter="\t")

        for k, v in globs.word._dictionary.items():
            wor_w.writerow([v, k])
        for k, v in globs.lemma._dictionary.items():
            lem_w.writerow([v, k])


if __name__ == "__main__":
    data_file_msg = f"processing file  '{green}{DATA_F}{end}'"
    write_dir_msg = f"writing to dir   '{green}{PREFIX}{end}'"
    print()
    user_confirmation(
        data_file_msg + \
        "\n"          + \
        write_dir_msg + \
        "\n\ncontinue (y/Y)?"
    )

    main()
