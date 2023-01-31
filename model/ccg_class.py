from __future__ import annotations
from tkinter.messagebox import NO
from typing import Any, NoReturn
from nltk.sem.logic import Expression  # type: ignore
import string

read_expr = Expression.fromstring  # type: ignore


class leaf:
    """Leaf"""


    def __init__(self, raw_str: str, depth: int, spacy_info: Any) -> None:
        self.raw_str: str = raw_str
        self.depth: int = depth
        self.spacy_info = spacy_info

        self.spacy_t: str = spacy_info["t"]
        self.spacy_l: str = spacy_info["l"]
        self.spacy_p: str = spacy_info["p"]

        self.filter_raw_str(raw_str[:-1])

        self.alphabet_upper: list[str] = [x.upper() for x in list(string.ascii_lowercase)]
        self.alphabet_lower: list[str] = list(string.ascii_lowercase)
        self.variables_lower: set[Any] = set()
        self.variables_upper: set[Any] = set()

        self.lambda_formula = None
        self.set_lambda_formula()

    def filter_raw_str(self, inp_str: str) -> None:
        """
        filter_str Filter a string into CCG, dutch word and lemma

        Args:
            inp_str (str): input raw string of CCG tree

        Returns:
            tuple[str, str, str]: Tuple with inside CCG semantics, Dutch word and lemma
        """
        self.semantics: str
        self.word: str
        self.lemma: str

        if "\\'" in inp_str:
            self.semantics = inp_str.split("'")[0][2:-2].upper()
            self.semantics_info()
            self.word = '\''.join(inp_str.split("'")[1:3])
            self.lemma = '\''.join(inp_str.split("'")[4:6])

        else:
            self.semantics = inp_str.split("'")[0][2:-2].upper()
            self.semantics_info()

            self.word = inp_str.split("'")[1]
            self.lemma = inp_str.split("'")[3]

        self.word = self.word.replace('-', '')
        self.word = self.word.replace(r'\'', '')

    def semantics_info(self) -> None:
        """
        semantics_info Cleans the semantics

        removes extra information from the ccg parses
        fix in the future to store this info somewhere

        Args:
            semantics (str): semantics input string

        Returns:
            str: cleaned input string
        """
        replace_list: list[str] = ["DCL", "TO",
                                   "ADJ", "B", "PSS", "PT", "NG", "EM"]
        for replace_word in replace_list:
            self.semantics = self.semantics.replace(f":{replace_word}", "")

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
            return f"({self.lambda_formula})"
        else:
            return f"[{self.word}]"

    def get_new_lower_variable(self) -> str:
        """
        get_new_lower_variable used by to_lambda to give new variable letter to each template

        Returns:
            str: unique letter
        """
        if 'z' in self.variables_lower:
            self.variables_lower = set()

        for letter in self.alphabet_lower:
            if letter not in self.variables_lower:
                self.variables_lower.add(letter)
                return letter
        

    def get_new_upper_variable(self) -> str:
        """
        get_new_upper_variable  used by to_lambda to give new variable letter to each template

        Returns:
            str: unique letter
        """
        if 'Z' in self.variables_upper:
            self.variables_upper = set()

        for letter in self.alphabet_upper:
            if letter not in self.variables_upper:
                self.variables_upper.add(letter)
                return letter

    def set_lambda_formula(self) -> None:
        """
        set_lambda_formula Set the lambda_formula to the expression, according to the lemma, semantics and POS
        sets lambda_formula of this object
        """
        P: str = None
        Q: str = None
        x: str = None
        self.lambda_formula: Any
        # print(f'self.word: {self.word}, self.semantics: {self.semantics}, self.POS: {self.spacy_p}')

        forbidden_lst: list[str] = [r"\'", "-", ","]

        for forbidden in forbidden_lst:
            if forbidden in self.word:
                # For \' simply remove it from the string
                # if not forbidden == r'\'':
                #     return
                
                self.word.replace(r'\'', '')
                self.word.replace('-', '')
                # FIXME
                # print(f"Error with parsing string: {self.word}. Forbidden word found")

        print(f'word: {self.word.lower()}, semantic: {self.semantics}, pos: {self.spacy_p}')

        match (self.word.lower(), str(self.semantics), self.spacy_p):

            case (word, r"((S\NP)/NP)", pos) | (word, r"(S\NP)/NP", pos) | (word, "VP/NP", pos):
                print(r'word, r"((S\NP)/NP)", pos')
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                x = self.get_new_lower_variable()
                self.lambda_formula = read_expr(
                    rf"\{P}.\{Q}.(exists {x}.({P}({x}) & {Q}({x})))"
                    )

            case ('sommige', "PP/NP", pos):
                print('sommige, PP/NP')
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                x = self.get_new_lower_variable()
                self.lambda_formula = read_expr(
                    rf"\{P}.\{Q}. (exists {x} . ({P}({x}) -> {Q}({x})))")

            case ('sommige', sem, pos):
                print('sommige, rest')
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                x = self.get_new_lower_variable()
                self.lambda_formula = read_expr(
                    rf"\{P}.\{Q}. (exists {x} . ({P}({x}) -> {Q}({x})))")

            case ('alle', "NP/N", pos) | ('elke', "NP/N", pos):
                print(r'alle/elke, NP/N')
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                x = self.get_new_lower_variable()
                self.lambda_formula = read_expr(
                    rf"\{P}.\{Q}. (all \{x} . (\{P}(\{x}) -> \{Q}(\{x})))")

            case ('of', sem, pos):
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                self.lambda_formula = read_expr(
                    rf"\{P}.\{Q}.({P} | {Q})"
                )

            case ('en', sem, "CCONJ"):
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                self.lambda_formula = read_expr(
                    rf"\{P}.\{Q}.({P} & {Q})"
                )

            case ('een', "NP/N", "DET"):
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                x = self.get_new_lower_variable()
                self.lambda_formula = read_expr(
                    rf"\{P}\{Q}.(exists {x}.({P}({x}) & {Q}({x})))"
                )

            case ('in', 'PP/NP', 'ADP') | ('in', r"((S\NP)\(S\NP))/NP", 'ADP'):
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                R = self.get_new_upper_variable()
                x = self.get_new_lower_variable()

                self.lambda_formula = read_expr(
                    rf"\{P}.\{Q}.({P} (\{R}.(in({Q}, {R}))))"
                )

            case (word, "S\S", "NOUN"):
                v1 = self.get_new_upper_variable()
                self.lambda_formula = read_expr(
                    rf"\{v1}.{v1}"
                )

            case (word, sem, "PRON"):
                v1 = self.get_new_upper_variable()
                v2 = self.get_new_upper_variable()
                x1 = self.get_new_lower_variable()
                x2 = self.get_new_lower_variable()
                
                self.lambda_formula = read_expr(
                    rf"\{v1} \{v2}((exists {x1} . ({v1} (exists {x2} . (persoon({x2}))) ({x1})) & ({v2} ({x1}))))"
                )

            case (word, 'PP/NP', 'ADP'):
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                R = self.get_new_upper_variable()
                x = self.get_new_lower_variable()

                self.lambda_formula = read_expr(
                    rf"\{P}.\{Q}.({P} (\{R}.({word}({Q}, {R}))))"
                )

            case (word, "NP/N", "DET"):
                P = self.get_new_upper_variable()

                self.lambda_formula = read_expr(
                    rf"\{P}.({P})"
                )

                # FIXME
                # raise NotImplementedError("MISSING: NP/N! word: ", word, " pos: ", pos)

            case ('niet', sem, 'ADV'):
                v1 = self.get_new_upper_variable()
                v2 = self.get_new_upper_variable()
                v3 = self.get_new_upper_variable()
                v4 = self.get_new_upper_variable()
                v5 = self.get_new_upper_variable()

                self.lambda_formula = read_expr(
                    rf"\{v1}. \{v2}. \{v3}. ({v2} (\{v4}.-(((({v1}(\{v5}.({v5}({v4})))))))))"
                ) #                     rf"\{v1}. \{v2}. \{v3}. ({v2} (\{v4}.-(((({v1}(\{v5}.({v5}({v4}))))) {v3})))"
                # self.lambda_formula = read_expr(
                #     rf"\v1.(-v1)"
                # )

            case(word, 'N/PP', pos):
                v1 = self.get_new_upper_variable()
                v2 = self.get_new_upper_variable()
                v3 = self.get_new_upper_variable()
                x1 = self.get_new_lower_variable()
                x2 = self.get_new_lower_variable()

                self.lambda_formula = read_expr(
                    rf"\{v1}.\{v2}.({word}({v2}) & {v1} ({v2}))"
                )


            case (word, sem, "DET"):
                P = self.get_new_upper_variable()
                
                self.lambda_formula = read_expr(
                    rf"\{P}.({P})"
                )

            case ('is', sem, pos):
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                self.lambda_formula = read_expr(
                    rf"\{P}.\{Q}.{P}({Q})"
                )

            case (word, r"(NP\NP)/NP", "CCONJ"):
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                self.lambda_formula = read_expr(
                    rf"\{P}\{Q}.{P}&{Q}"
                )

            case (word, "PP/NP", "SCONJ"): # in, naar 
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                self.lambda_formula = read_expr(
                    rf"\{P}\{Q}.{P}&{Q}"
                )

            case (word, sem, "PUNCT"):
                P = self.get_new_upper_variable()
                self.lambda_formula = read_expr(
                    rf"\P.P"
                )

            case (word, r"(S\NP)", pos) | (word, r"S\NP", pos):
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                x = self.get_new_lower_variable()
                self.lambda_formula = read_expr(
                    rf"\{P} . ({P}(\{x}.{word}({x})))")

            case (word, sem, "VERB"):
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                x = self.get_new_lower_variable()
                self.lambda_formula = read_expr(
                    rf"\{P}.\{Q}.(exists {x}.({P}({x}) & {Q}({x})))"
                    )

            case (word, "N", pos):
                x = self.get_new_lower_variable()
                self.lambda_formula = read_expr(rf"\{x}.{word}({x})")

            case (word, sem, "ADJ"):
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                x = self.get_new_lower_variable()
                self.lambda_formula = read_expr(
                    rf"\{P}.\{Q}.(exists {x} . ({word}({x})) & ({P} ({Q})))"
                )

            case (word, sem, "ADP"):
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                self.lambda_formula = read_expr(
                    rf"\{P}\{Q}.{P}&{Q}"
                )

            case (word, 'N/NP', pos):
                pass

            case (word, sem, 'NUM'):
                P = self.get_new_upper_variable()
                Q = self.get_new_upper_variable()
                x = self.get_new_lower_variable()

                self.lambda_formula = read_expr(
                    rf"\{P}.\{Q}. (exists {x} . ({word}({x})) & ({P} ({Q})))"
                )


            case (word, sem, pos):
                pass

        if self.lambda_formula is None:
            print('-------- No lambda for the previous sentence')
            pass


    def find_child(self, *args: Any) -> NoReturn:
        """
        find_child Impossible function, should not be called
        """
        raise RuntimeError("Entered leaf during child search")

    def print(self, *args: Any) -> str:
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
        return f"{self.word}"

    def __repr__(self) -> str:
        return self.print()


class tree:
    """Tree structure"""

    def __init__(self, name: str, depth: int,
                 parent: 'tree' | None,
                 left: leaf | tree | None,
                 right: leaf | tree | None) -> None:
        self.name: str = name
        self.depth: int = depth
        self.parent: tree | None = parent
        self.left: leaf | tree | None = left
        self.right: leaf | tree | None = right

        self.filter_str(name)

    def filter_str(self, raw_str: str) -> None:
        """
        filter_str extracts the action, ccg and lx from the raw string

        finds the action of a CCG line, stored in action
        finds the ccg phrase itself, stored in ccg
        and if the term is LX, stores that in lx

        Args:
            raw_str (str): the raw string from the prolog file
        """
        self.label: str
        self.ccg: str
        self.lx: str = ""

        self.label = raw_str.split("(")[0]
        self.ccg = raw_str.split(",")[0]
        self.ccg = self.ccg[self.ccg.find("(") + 1:]

        if raw_str.count(",") == 2:
            self.lx = raw_str.split(",")[-2].strip()

    def add_tree(self, name: str) -> tree:
        """
        add_tree Adds a tree to children

        Args:
            name (str): tree name
        """
        if self.left is None:
            self.left = tree(name=name,
                             parent=self,
                             depth=self.depth + 1,
                             left=None,
                             right=None)
            return self.left

        elif self.right is None:
            self.right = tree(name=name,
                              parent=self,
                              depth=self.depth + 1,
                              left=None,
                              right=None)
            return self.right
        else:
            raise TypeError("Three children found")

    def add_leaf(self, name: str, spacy_info: Any) -> None:
        """
        add_leaf adds a leaf to the current tree
        Args:
            name (str): name of the leaf
        """
        if self.left is None:
            self.left = (leaf(raw_str=name,
                              depth=self.depth + 1,
                              spacy_info=spacy_info))
        elif self.right is None:
            self.right = (leaf(raw_str=name,
                               depth=self.depth + 1,
                               spacy_info=spacy_info))
        else:
            raise TypeError("Three children found")

    def get_parent_tree(self) -> tree | None:
        """
        get_parent_tree get the tree of the parent, if it exists

        Returns:
            tree : pointer
        """
        return self.parent

    def find_parent(self, depth: int) -> tree:  # type: ignore
        """
        find_parent Find the most recent added tree child node at the appropiate depth

        Args:
            depth (int): at what depth the tree should find the most recent child

        Returns:
            tree: returns a tree class
        """
        if depth == self.depth:
            return self
        else:
            return self.parent.find_parent(depth)  # type: ignore

    def root(self) -> tree:
        """
        root gives back a pointer to the root of the tree

        finds the root and returns it

        Returns:
            tree: Highest possible parent
        """
        if self.get_parent_tree() is None:
            return self
        else:
            return self.get_parent_tree().root()  # type: ignore

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
        if self.label == "lx":
            # check if leaf lambda formula is not none
            if lambda_formule and type(self.left) == leaf:
                # FIXME
                if self.left.lambda_formula is None:
                    raise NotImplementedError("Lambda Expression is None")
            return rf"({self.left.make_lambda(lambda_formule=lambda_formule)})"
        else:
            if lambda_formule and type(self.left) == leaf:
                # FIXME
                if self.left.lambda_formula is None:
                    raise NotImplementedError("Lambda Expression is None")

            if lambda_formule and type(self.right) == leaf:
                # FIXME
                if self.right.lambda_formula is None:
                    raise NotImplementedError("Lambda Expression is None")

            left: str = self.left.make_lambda(lambda_formule=lambda_formule)
            right: str = self.right.make_lambda(lambda_formule=lambda_formule)

            if self.label == "fa":
                # Forward application
                return rf"({left} {right})"

            elif self.label == "ba":
                # backward application
                return rf"({right} {left})"

            elif self.label == "fc":
                # Forward composition
                return rf"(\x.{left} ({right}x))"

            elif self.label == "bc":
                # Backward composition
                return rf"(\x.{right} ({left}x))"

            elif self.label == "fxc":
                # Forward crossing composition
                return rf"(\x.{right} ({left}x))"

            elif self.label == "fxc":
                # Backward crossing composition
                return rf"(\x.{right} ({left}x))"
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
        left_str: str
        right_str: str
        if self.left is None:
            left_str = "None"
        else:
            left_str = self.left.print(depth + 1)

        if self.right is None:
            right_str = "None"
        else:
            right_str = self.right.print(depth + 1)

        tab_str: str = '|\t' * depth
        return f"label: {self.label}\n \
    {tab_str}left: {left_str}\n \
    {tab_str}|\n \
    {tab_str}right: {right_str}"

    def __repr__(self) -> str:
        return self.print()
