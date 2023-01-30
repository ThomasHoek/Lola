# type: ignore
import os
import nltk
from nltk.sem import Expression
from typing import List

read_expr = Expression.fromstring

# load data
dir_path: str = os.path.dirname(os.path.realpath(__file__))


def prover9_prove(conclusion: str, premises: List[str] = [], path=rf"{dir_path}/../prover9/bin-win32") -> bool:
    """
    Give a conclusion and a list of premises, builds a tableau and
    detects whether the premises entail the conclusion.
    Returns a boolean value and optionally prints the tableau structure
    """
    str2exp = nltk.sem.Expression.fromstring
    c = str2exp(conclusion)
    ps = [str2exp(p) for p in premises]
    prover9 = nltk.Prover9()

    if path:
        prover9.config_prover9(path)

    return prover9.prove(c, ps)


print(prover9_prove("some y. not man(y)", ["all x.(man(x) -> walks(x))", "not walks(Alex)"]))

valid_fol = "exists x. (L(x) & exists y. (E(y) & y = x)) -> exists x.(L(x) & E(x))"

# prover9 handles equality properly
print(prover9_prove(valid_fol))
