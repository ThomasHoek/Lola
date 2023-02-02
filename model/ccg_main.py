from typing import IO, Any
import ccg_parse
from ccg_class import tree
import pickle
from nltk.sem.logic import Expression, LogicalExpressionException, ApplicationExpression  # type: ignore
read_expr = Expression.fromstring  # type: ignore


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

    simplified_dict: dict[int, str] = {}

    error: int = 0
    lambda_count: int = 0

    for i, ccg_tree in enumerate(class_lst):
        try:
            ccg_str_simp = ccg_tree.make_lambda()

            if "\\" in str(ccg_str_simp):
                lambda_count += 1

        except NotImplementedError:
            error += 1
            ccg_str_simp = "error"

        except LogicalExpressionException:
            error += 1
            ccg_str_simp = "error"

        simplified_dict[i] = ccg_str_simp

    print(f"Completed with {error} amount of errors.")
    print(f"{len(class_lst) - error} parsing succesful.")
    print(f"{len(class_lst) - error - lambda_count} FOL statements dont contain lambda.")

    return simplified_dict


def write_ccg_to_file(ccg_dict: dict[int, ApplicationExpression]) -> None:
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

    for i in range(len(ccg_dict)):
        try:
            output_file.write(r"{}".format(str(ccg_dict[i]) + "\n"))

            if ccg_dict[i] != "error":
                correct_file.write(str(i) + "\n")

        except LogicalExpressionException:
            output_file.write(r"error | {}".format(ccg_dict[i] + "\n"))

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

    simp_dict = get_ccg_dict()

    if write:
        write_ccg_to_file(simp_dict)
