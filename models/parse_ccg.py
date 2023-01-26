import nltk.tree.tree
from nltk.tree.tree import Tree as tree_class_type
from nltk.ccg.lexicon import Token as token_class_type
from ccg_classes import leaf_info
from parse_tree import parse_tree
# list | str


def print_leaf_lst(inp) -> str:
    string: str = f""

    if type(inp) == list:
        first = print_leaf_lst(inp[0])
        second = print_leaf_lst(inp[1])
        string = f"({first}@{second})"
    else:
        string = f"[[{inp.word} | {inp.semantics}]]"

    return string


def recursive_leaves(self):
    leaf_lst = []

    # if another tree
    if len(self) == 2:
        token, label = self.label()
        first = self[0].recursive_leaves()
        second = self[1].recursive_leaves()

        # check type
        if label == ">":
            leaf_lst = [first, second]

        elif label == "<":
            leaf_lst = [second, first]

        elif label == ">B":
            leaf_lst = [second, first]

    else:
        # tree only contains nodes
        return leaf_info(self)
        # return "[" + str(self[0]) + " | " + str(self.label()) + "]"

    return leaf_lst


tree_class_type.recursive_leaves = recursive_leaves


if __name__ == "__main__":
    data = r'''
ccg(84,
 ba(s:dcl,
  fa(np,
   t(np/n, 'Een', [lemma:'een']),
   t(n, 'man', [lemma:'man'])),
  fa(s:dcl\np,
   t((s:dcl\np)/pp, 'zit', [lemma:'zit']),
   fa(pp,
    t(pp/np, 'in', [lemma:'in']),
    fa(np,
     t(np/n, 'een', [lemma:'een']),
     t(n, 'veld', [lemma:'veld'])))))).
     ccg(263,
 ba(s:dcl,
  fa(np,
   t(np/n, 'Sommige', [lemma:'sommige']),
   t(n, 'mensen', [lemma:'mensen'])),
  t(s:dcl\np, 'lopen', [lemma:'lopen']))).
'''

    parse = parse_tree("Een man zit in een veld", data)
    test_var = parse.recursive_leaves()
    print(print_leaf_lst(test_var))