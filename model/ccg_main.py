from typing import IO, Any
import ccg_parse
from ccg_class import tree
import pickle
from nltk.sem.logic import Expression  # type: ignore

read_expr = Expression.fromstring  # type: ignore


def brackets_check(input_str: str) -> bool:
    """
    brackets_check check if the amount of brackets are logically right

    Using a stack, checks if the build with open brackets is the same as the
    debuild using closed brackets.

    Args:
        input_str (str): input string

    Returns:
        bool: a boolean to see if the check passed
    """
    stack: list[str] = []

    for character in input_str:
        if (character == '('):
            stack.insert(0, ')')

        elif (character == '['):
            stack.insert(0, ']')

        elif (stack != [] and character == stack[0]):
            stack.pop(0)

        elif (character == ')' or character == ']'):
            print(character, stack)
            print(input_str)
            return False

    # stack empty
    return stack == []


if __name__ == "__main__":
    import sys
    import os

    try:
        write: bool = sys.argv[1] == "write"
    except IndexError:
        write: bool = False

    dir_path: str = os.path.dirname(os.path.realpath(__file__))

    ccg_file: IO[Any] = open(
        f"{dir_path}/../input/pmb_ccg.pl", encoding="utf-8")
    ccg_data: list[list[tuple[int, str]]] = ccg_parse.parse_data(ccg_file)
    ccg_file.close()

    spacy_file: IO[Any] = open(
        f"{dir_path}/../input/spacy_lg.json", encoding="utf-8")
    class_lst: list[tree] = ccg_parse.parse_class(ccg_data, spacy_file)
    spacy_file.close()

    # print(class_lst[0])
    # print(class_lst[0].print_lambda())

    ccg_str: str
    ccg_info_dict: dict[int, str] = {}

    error: int = 0
    for i, ccg_tree in enumerate(class_lst):
        try:
            ccg_str = ccg_tree.make_lambda()
            assert brackets_check(ccg_str)
        except NotImplementedError:
            error += 1
            ccg_str = "error"
        ccg_info_dict[i] = ccg_str

    print(f"Completed with {error} amount of errors.")
    print(f"{len(class_lst) - error} succesful.")

    if write:
        with open(f"{dir_path}/../output/ccg_info_pickle", 'wb') as f:
            pickle.dump(class_lst, f)

        correct_file: IO[Any] = open(
            f"{dir_path}/../output/correct.txt", "w+", encoding="utf-8")

        output_file: IO[Any] = open(
            f"{dir_path}/../output/output.py", "w+", encoding="utf-8")
        for i in range(len(ccg_info_dict)):
            lambda_simp: Any = read_expr(ccg_info_dict[i]).simplify()
            output_file.write(r"{} | {}".format(
                lambda_simp, ccg_info_dict[i] + "\n"))

            if ccg_info_dict[i] != "error":
                correct_file.write(str(i) + "\n")
        output_file.close()
        correct_file.close()
