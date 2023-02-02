# type: ignore
from cProfile import label
import os
import nltk
from tqdm import tqdm
from nltk.sem import Expression
from nltk.sem import ApplicationExpression
from nltk.sem.logic import LogicalExpressionException
from typing import IO, Any
from ccg_main import get_ccg_dict
from ccg_parse import parse_SICK_NL, parse_assumptions
read_expr = Expression.fromstring

# load data
dir_path: str = os.path.dirname(os.path.realpath(__file__))


def prover9_prove(conclusion: ApplicationExpression, premises: list[ApplicationExpression] = [], path=rf"{dir_path}/../prover9/bin-win32") -> bool:
    """
    Give a conclusion and a list of premises, builds a tableau and
    detects whether the premises entail the conclusion.
    Returns a boolean value and optionally prints the tableau structure
    """
    prover9 = nltk.Prover9()

    if path:
        prover9.config_prover9(path)

    return prover9.prove(conclusion, premises), prover9


if __name__ == "__main__":
    assumption_lst: list[str] = parse_assumptions()
    # impl(boom,plant)
    assumption_clean = []

    # add premises
    for x in assumption_lst:
        try:
            assumption_clean.append(read_expr(x).simplify())
        except LogicalExpressionException:
            # print(x, " failed")
            pass

    print("-----------CCG-----------")
    # get all sentences and parse them
    SICK_NL_test_file: IO[Any] = open(rf"{dir_path}\..\input\sen.pl", "r")
    sick_dataset = parse_SICK_NL(SICK_NL_test_file)
    SICK_NL_test_file.close()

    # get CCG info
    ccg_dict: dict[int, str]
    _, ccg_dict = get_ccg_dict()

    # file to write anwers to
    solve_file: IO[Any] = open(rf"{dir_path}\..\output\solve.py", "w+")

    # counters to see the ratio of fail and succes
    error_counter: int = 0
    parse_fail_counter: int = 0
    correct_parsed_counter: int = 0
    correct_label: int = 0
    entail_label: int = 0
    contradict_label: int = 0
    neutral_label: int = 0

    print("-----------FOL-----------")

    # for each problem
    for task in tqdm(sick_dataset):
        # get info
        problemID, hypothesis, premise, dataset, solution = task
        hypothesis = ccg_dict[hypothesis - 1]
        premise = ccg_dict[premise - 1]

        # if hypothesis fails
        if dataset != "TEST":
            continue

        # write info to file
        solve_file.write(f"{problemID} | {solution}\n")
        solve_file.write(f"h: {hypothesis}\n")
        solve_file.write(f"p: {premise}\n")


        if hypothesis == "error" or premise == "error":
            solve_file.write("s: error\n")
            error_counter += 1

        else:
            hypo_assumption: list[str] = assumption_clean + [hypothesis]
            r_premise = ApplicationExpression(
                read_expr(r"\x. -x"), premise).simplify()

            try:
                true_solution_return, info = prover9_prove(
                    premise, hypo_assumption)

                false_solution_return, info = prover9_prove(
                    r_premise, hypo_assumption)

                solve_file.write("s:{} | {} \n".format(
                    true_solution_return, false_solution_return))
                correct_parsed_counter += 1

                if solution == "yes":
                    if true_solution_return and not false_solution_return:
                        correct_label += 1
                        entail_label += 1

                elif solution == "no":
                    if not true_solution_return and false_solution_return:
                        correct_label += 1
                        contradict_label += 1

                elif solution == "unknown":
                    if not true_solution_return and not false_solution_return:
                        correct_label += 1
                        neutral_label += 1

            except Exception as e:
                solve_file.write(f"s: {e}\n")
                parse_fail_counter += 1

        solve_file.write("------------------------------\n")

    solve_file.close()

    print(f"{error_counter} cases with errors")
    print(f"{parse_fail_counter} cases where parse gave errors")
    print(f"{correct_parsed_counter} cases parsed correctly")
    print(f"{correct_label}  labels correct")
    print(f"{entail_label}  entailment correct")
    print(f"{contradict_label}  contradict correct")
    print(f"{neutral_label}  neutral correct")

