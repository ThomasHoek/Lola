# type: ignore | pylance
# import nltk.tree.tree
# from nltk.ccg.lexicon import Token as token_class_type
from nltk.tree.tree import Tree as tree_class_type
from ccg_classes import tree_info, leaf_info
from parse_tree import parse_tree


def recursive_leaves(self):
    """
    recursive_leaves Function to recursively parse the NLTK format

    The normal NLTK functions iterates using a for loop.
    This function reads the NLTK format and parses it into our classes of a tree and node.

    Returns:
        tree_info: self made class that stores information in a tree, leaf structure
    """
    leaf_lst = []

    # if another tree
    if len(self) == 2:
        token, label = self.label()
        first = self[0].recursive_leaves()
        second = self[1].recursive_leaves()

        return tree_info(first, second, label)

    # tree only contains nodes
    else:
        # TODO: this might break for type-raising
        # but that has yet to be implemented
        return leaf_info(self)

    return leaf_lst


# add function to NLTK library
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
    # get data from laura
    parse = parse_tree("Een man zit in een veld", data)

    # parse data into tree/leaf format
    tree_parse = parse.recursive_leaves()

    print(tree_parse.print())
    print(tree_parse.print_lambda(False))
