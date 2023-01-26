from __future__ import annotations
from nltk.sem.logic import * 
import string

read_expr = Expression.fromstring


alphabet_upper = [x.upper() for x in list(string.ascii_lowercase)]
alphabet_lower = list(string.ascii_lowercase)
variables_lower = set()
variables_upper = set()

# used by to_lambda to give new variable letter to each template
def get_new_lower_variable():
    for letter in alphabet_lower:
        if letter not in variables_lower:
            variables_lower.add(letter)
            return letter
    return 'x'

def get_new_upper_variable():
    for letter in alphabet_upper:
        if letter not in variables_upper:
            variables_upper.add(letter)
            return letter
    return 'P'


class tree_info():
    """
    tree class to parse the NLTK format into something usable
    """

    def __init__(self,
                 left: tree_info | leaf_info,
                 right: tree_info | leaf_info,
                 label: str) -> None:
        self.left: tree_info | leaf_info = left
        self.right: tree_info | leaf_info = right
        self.label: str = label

    def make_lambda(self, lambda_formule: bool = True) -> str:
        """
        make_lambda transforms the tree structure into a lambda string

        Recursively builds down the tree into the leaf structures finding the lambda/word.
        Then builds back the lambda expression making use of the label / ccg information.
        Returns all the info back into a string of the tree and children properly parsed.

        Args:
            lambda_formule (bool, optional): if false prints the word itself
                                             if true prints the lambda formule.
                                             Defaults to True.

        Returns:
            str: output string
        """
        left: str = self.left.make_lambda(lambda_formule=lambda_formule)
        right: str = self.right.make_lambda(lambda_formule=lambda_formule)

        if self.label == ">":
            return rf"({left}@{right})"

        elif self.label == "<":
            return rf"({right}@{left})"

        elif self.label == ">B":
            return rf"(\x.{left}@({right}@x))"

        elif self.label == "<B":
            return rf"(\x.{right}@({left}@x))"

        elif self.label == "<Bx":
            return rf"(\x.{right}@({left}@x))"

        elif self.label == ">Bx":
            return rf"(\x.{right}@({left}@x))"
        else:
            raise NotImplementedError(self.label, " not found")

    def print_lambda(self) -> str:
        """
        print_lambda Function to print the lambda rule

        Returns:
            str: output string
        """
        return self.make_lambda(lambda_formule=False)

    def print(self, depth: int = 0) -> str:
        """
        print Prints the tree's down in the linux LS format

        prints the trees down using depth in tabs where trees give info about:
            label, left tree and right tree
        and nodes give info about:
            word and semantics

        Args:
            depth (int, optional): Used to print the depth of the lower trees/nodes. Defaults to 0.

        Returns:
            str: returns a string of all the information
        """
        tab_str: str = '\t' * depth
        return f"label: {self.label}\n \
    {tab_str}left: {self.left.print(depth + 1)}\n \
    {tab_str}right: {self.right.print(depth + 1)}"

    def __repr__(self) -> str:
        return f"[left: {self.left.print()}, right: {self.right.print()}, label: {self.label}]"


class leaf_info():
    """
    leaf class to store info from the  NLTK format
    """

    lambda_formula = None # set by set_lambda
    POS = None

    def __init__(self, tree) -> None:  # type: ignore
        """
        __init__ Parses a NLTK tree into leafs

        Args:
            tree (NLTK.tree.tree.tree): NLTK tree structure after parsing

        Sets:
            self.semantics (str): Info about semantics
            self.word (str): info about the word
        """
        self.semantics: str
        self.semantics, _ = tree.label()  # type: ignore
        child: list[str]
        for child in tree:
            for child2 in child:
                self.word: str = child2

    def set_lambda_formula(self) -> None:
        """
        set_lambda_formula Set the lambda_formula to the expression, according to the lemma, semantics and POS  
        Args:
            lambda_formula (str): sets lambda_formula of this object
        """
        print(f'self.word: {self.word}, self.semantics: {self.semantics}, self.POS: {self.POS}')
        match (self.word.lower(), str(self.semantics), self.POS):
            
            case (word, r"((S\NP)/NP)", pos) | (word, "VP/NP", pos):
                print('Does not work yet')
                var_1 = get_new_upper_variable()
                var_2 = get_new_upper_variable()
                var_3 = get_new_lower_variable()
                self.lambda_formula = read_expr(rf"\P\Q.(S(\x.(O(\y.{word}(x,y)))))")

            case ('sommige', "PP/NP", pos):
                P = get_new_upper_variable()
                Q = get_new_upper_variable()
                x = get_new_lower_variable()
                self.lambda_formula = read_expr(rf"\{P}.\{Q}. (exists {x} . ({P}({x}) -> {Q}({x})))")
            
            case ('sommige', sem, pos):
                P = get_new_upper_variable()
                Q = get_new_upper_variable()
                x = get_new_lower_variable()
                self.lambda_formula = read_expr(rf"\{P}.\{Q}. (exists {x} . ({P}({x}) -> {Q}({x})))")

            case ('alle', "NP/N", pos):
                P = get_new_upper_variable()
                Q = get_new_upper_variable()
                x = get_new_lower_variable()
                self.lambda_formula = read_expr(rf"\{P}.\{Q}. (all \{x} . (\{P}(\{x}) -> \{Q}(\{x})))")

            case (word, "NP/N", pos):
                print(f'MISSING: NP/N! word: {word}, pos: {pos}')

            case (word, r"(S\NP)", pos) | (word, r"S\NP", pos):
                P = get_new_upper_variable()
                Q = get_new_upper_variable()
                x = get_new_lower_variable()
                self.lambda_formula = read_expr(rf"\{P} . ({P}(\{x}.{word}({x})))")
                
                
            case (word, "N", pos):
                x = get_new_lower_variable()
                self.lambda_formula = read_expr(rf"\{x}.{word}({x})")

            case (word, sem, pos):
                print(f'Missing (default): {word}, {sem}, {pos}')

    def make_lambda(self, lambda_formule: bool = True) -> str:
        """
        make_lambda transforms the tree structure into a lambda string

        Recursively builds down the tree into the leaf structures finding the lambda/word.
        Then builds back the lambda expression making use of the label / ccg information.
        Returns all the info back into a string of the tree and children properly parsed.

        Args:
            lambda_formule (bool, optional): if false prints the word itself
                                             if true prints the lambda formule.
                                             Defaults to True.

        Returns:
            str: output string
        """
        if lambda_formule:
            return f"[{self.lambda_formule}]"
        else:
            return f"[{self.word}]"

    def print(self, depth: int = 0) -> str:
        """
        print Prints the tree's down in the linux LS format

        prints the trees down using depth in tabs where trees give info about:
            label, left tree and right tree
        and nodes give info about:
            word and semantics

        Args:
            depth (int, optional): Used to print the depth of the lower trees/nodes. Defaults to 0.

        Returns:
            str: returns a string of all the information
        """
        tab_str: str = '\t' * depth
        return f"{tab_str}Word: {self.word} & sem: {self.semantics}"

    def __repr__(self) -> str:
        return self.word
