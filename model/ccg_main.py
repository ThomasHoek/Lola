from typing import IO, Any
import ccg_parse
from ccg_class import tree
import pickle
from nltk.sem.logic import Expression, LogicalExpressionException  # type: ignore
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


def get_ccg_dict() -> tuple[dict[int, str], dict[int, str]]:
    """
    get_ccg_dict Get the CCG dictionary of lambda expressions

    returns the lambda expresions

    Returns:
        tuple[dict[int, str], dict[int, str]]: returns two dictionaries, long expression and simplified
    """
    import os
    dir_path: str = os.path.dirname(os.path.realpath(__file__))

    ccg_file: IO[Any] = open(
        f"{dir_path}/../input/pmb_ccg.pl", encoding="utf-8")
    ccg_data: list[list[tuple[int, str]]] = ccg_parse.parse_data(ccg_file)
    ccg_file.close()

    spacy_file: IO[Any] = open(
        f"{dir_path}/../input/spacy_lg.json", encoding="utf-8")
    class_lst: list[tree] = ccg_parse.parse_class(ccg_data, spacy_file)
    spacy_file.close()

    ccg_str: str = ""
    ccg_info_dict: dict[int, str] = {}
    simplified_dict: dict[int, str] = {}

    error: int = 0
    simperror: int = 0
    lambda_count: int = 0

    for i, ccg_tree in enumerate(class_lst):
        try:
            ccg_str = ccg_tree.make_lambda()
            assert brackets_check(ccg_str)

            ccg_str_simp: Any = read_expr(ccg_str).simplify()  # type: ignore

            if "\\" in str(ccg_str_simp):
                lambda_count += 1

        except NotImplementedError:
            error += 1
            simperror += 1
            ccg_str = "error"
            ccg_str_simp = "error"

        except LogicalExpressionException:
            simperror += 1
            ccg_str_simp = "error"

        ccg_info_dict[i] = ccg_str
        simplified_dict[i] = ccg_str_simp

    print(f"Completed with {error} amount of errors.")
    print(f"Completed with {simperror} amount of simplifying errors.")
    print(f"{len(class_lst) - error} parsing succesful.")
    print(f"{len(class_lst) - simperror} simplifying succesful.")
    print(f"{len(class_lst) - simperror - lambda_count} FOL statements dont contain lambda.")

    return ccg_info_dict, simplified_dict


def write_ccg_to_file(ccg_dict: dict[int, str]) -> None:
    """
    write_ccg_to_file write the CCG information to a file, mostly used for debugging

    Args:
        ccg_dict (dict[int, str]): input CCG dictionary
    """
    import os
    dir_path: str = os.path.dirname(os.path.realpath(__file__))

    with open(f"{dir_path}/../output/ccg_info_pickle", 'wb') as f:
        pickle.dump(ccg_dict, f)

    correct_file: IO[Any] = open(
        f"{dir_path}/../output/correct.txt", "w+", encoding="utf-8")

    output_file: IO[Any] = open(
        f"{dir_path}/../output/output.py", "w+", encoding="utf-8")

    simplified_file: IO[Any] = open(
        f"{dir_path}/../output/simplified.py", "w+", encoding="utf-8")

    for i in range(len(ccg_dict)):
        try:
            lambda_simp: Any = read_expr(r"{}".format(ccg_dict[i])).simplify()  # type: ignore

            output_file.write(r"{} | {}".format(
                lambda_simp, ccg_dict[i] + "\n"))

            simplified_file.write(r"{}".format(lambda_simp))
            simplified_file.write("\n")

            if ccg_dict[i] != "error":
                correct_file.write(str(i) + "\n")

        except LogicalExpressionException:
            output_file.write(r"error | {}".format(
                ccg_dict[i] + "\n"))
            simplified_file.write("error\n")

    output_file.close()
    correct_file.close()


if __name__ == "__main__":
    import sys

    try:
        write: bool = sys.argv[1] == "write"
    except IndexError:
        write: bool = False

    long_dict: dict[int, str]
    simp_dict: dict[int, str]

    long_dict, simp_dict = get_ccg_dict()

    if write:
        write_ccg_to_file(long_dict)
