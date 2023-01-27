from typing import IO, Any
from ccg_class import tree
import json


def parse_data(ccg_file: IO[Any]) -> list[list[tuple[int, str]]]:
    """
    parse_data Parses aprolog tree into a python structure

    converts the structure into a list of CCG elements.
    These CCG elements contain of a list of each specific row.
    Each row has information stored in a tuple format.
    The tuple contains the depth and the raw string

    Args:
        ccg_file (IO[Any]): a file with CCG info

    Returns:
        list[list[tuple[int, str]]]: Python format specified above
    """
    # remove prolog comments and strip the end away
    ccg_data: list[str] = [x.rstrip("\n")
                           for x in ccg_file.readlines() if x[0] != ":"]

    # replace amount of indents with a number and set split tokens
    split_token: str = "+SPLIT+"
    ccg_data_indent_num: list[tuple[int, str] | str] = [(len(x) - len(x.lstrip()), x.strip())
                                                        if x != ""
                                                        else split_token
                                                        for x in ccg_data]

    # split into chunk based on split_token (not included)
    cgg_parse: list[list[tuple[int, str]]] = [[]]

    counter: int = 0

    for line in ccg_data_indent_num:
        if line == split_token:
            counter += 1
            cgg_parse.append([])
        else:
            # is correctly typed, but pylance does not recognise
            assert type(line) == tuple
            cgg_parse[counter].append(line)  # type: ignore

    # remove empty lists
    return [x for x in cgg_parse if x]


def parse_class(ccg_data: list[list[tuple[int, str]]], spacy_file: IO[Any]) -> list[tree]:
    """
    parse_class Parses the python structure into a tree and leaf class

    Converts the lists of lists with tuples from the parse_data function into a tree structure.
    Exists out of tree and leaf classes.

    Args:
        ccg_data (list[list[tuple[int, str]]]): Python structure after prolog convert

    Returns:
        list[tree]: A list of lists containing tree's
    """
    # ready spacy and set param info
    spacy_info: Any = json.load(spacy_file)

    ccg_lst: list[tree] = []
    for spacy_ccg_counter, ccg_tree in enumerate(ccg_data):
        spacy_leaf_counter: int = 0

        current: tree
        depth: int
        name: str

        depth, name = ccg_tree[1]
        current = tree(name=name,
                       depth=depth,
                       parent=None,
                       left=None,
                       right=None)

        for line in ccg_tree[2:]:
            depth, name = line

            # move current to appropiate level first
            # lazy method, looking up in parents is better
            if depth <= current.depth:
                current = current.find_parent(depth - 1)

            if name[0:2] == "t(":
                spacy_leaf_data = spacy_info[str(spacy_ccg_counter + 1)][spacy_leaf_counter]
                spacy_leaf_counter += 1
                current.add_leaf(name, spacy_leaf_data)
            else:
                current = current.add_tree(name=name)

        ccg_lst.append(current.root())
    return ccg_lst