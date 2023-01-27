from __future__ import annotations
from typing import Any, NoReturn, Callable


class leaf:
    """Leaf"""

    def __init__(self, raw_str: str, depth: int) -> None:
        self.raw_str: str = raw_str
        self.depth: int = depth

        self.filter_str(raw_str[:-1])

    def filter_str(self, inp_str: str) -> None:
        """
        filter_str Filter a string into CCG, dutch word and lemma

        Args:
            inp_str (str): input raw string of CCG tree

        Returns:
            tuple[str, str, str]: Tuple with inside CCG, Dutch word and lemma
        """
        self.ccg_type: str
        self.dutch_word: str
        self.lemma: str

        if "\\'" in inp_str:
            self.ccg_type: str = inp_str.split("'")[0][2:-2]
            self.dutch_word: str = '\''.join(inp_str.split("'")[1:3])
            self.lemma: str = '\''.join(inp_str.split("'")[4:6])

        else:
            self.ccg_type: str = inp_str.split("'")[0][2:-2]
            self.dutch_word: str = inp_str.split("'")[1]
            self.lemma: str = inp_str.split("'")[3]

    def find_child(self, *args: Any) -> NoReturn:
        """
        find_child Impossible function, should not be called
        """
        raise RuntimeError("Entered leaf during child search")

    def pprint(self) -> str:
        return f"{self.depth * ' '}{self.raw_str}\n"

    def print_leaves(self) -> str:
        """
        print_leaves Print specific for leafs

        only prints the leaves and ignores the tree structure

        Returns:
            str: returns the data inside the leaves
        """
        return f"{self.ccg_type}|{self.dutch_word}|{self.lemma}\n"

    def print_tree(self) -> str:
        """
        print_tree Print specific for trees

        only prints the tree and ignores the leaf structure

        Returns:
            str: returns empty
        """
        return ""

    def print_prolog(self, depth: int = 0) -> tuple[str, int]:
        """
        print_prolog returns a string of PL format

        Using only the action, CCG and LX from tree
        using only the ccg_type, dutch_word and lemma
        to build back the PL format by using depth
        to calculate the correct amount of brackets.

        Args:
            depth (int, optional): depth, used for brackets. Defaults to 0.

        Returns:
            str: string of PL format
        """
        return f"{' ' * self.depth}t({self.ccg_type}, '{self.dutch_word}', [lemma:'{self.lemma}'])", self.depth

    def return_expression(self) -> tuple[str, str]:
        return f"[\'{self.lemma}\']", self.ccg_type

    def __repr__(self) -> str:
        return f"{self.raw_str}, (depth, {self.depth})lmao"


class tree:
    """Tree structure"""

    def __init__(self, name: str, depth: int,
                 parent: 'tree' | None,
                 children: list[leaf | tree]) -> None:
        self.name: str = name
        self.depth: int = depth
        self.parent: tree | None = parent
        self.children: list[leaf | tree] = children

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
        self.action: str
        self.ccg: str
        self.lx: str = ""

        self.action = raw_str.split("(")[0]
        self.ccg = raw_str.split(",")[0]
        self.ccg = self.ccg[self.ccg.find("(") + 1:]

        if raw_str.count(",") == 2:
            self.lx = raw_str.split(",")[-2].strip()

    def add_tree(self, name: str) -> None:
        """
        add_tree Adds a tree to children

        Args:
            name (str): tree name
        """
        self.children.append(tree(name=name,
                                  parent=self,
                                  depth=self.depth + 1,
                                  children=[]))

    def add_leaf(self, name: str) -> None:
        """
        add_leaf adds a leaf to the current tree
        Args:
            name (str): name of the leaf
        """
        self.children.append(leaf(raw_str=name, depth=self.depth + 1))

    def get_parent_tree(self) -> tree | None:
        """
        get_parent_tree get the tree of the parent, if it exists

        Returns:
            tree : pointer
        """
        return self.parent

    def find_child(self, depth: int) -> tree:  # type: ignore
        """
        find_child Find the most recent added tree child node at the appropiate depth

        Args:
            depth (int): at what depth the tree should find the most recent child

        Returns:
            tree: returns a tree class
        """
        if depth == self.depth:
            return self
        else:
            for child in self.children[::-1]:
                if type(child) == tree:
                    return child.find_child(depth)

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

    def pprint(self) -> str:
        """
        pprint gives back the underlaying folders in a pretty format
        Returns:
            str: string formatted
        """

        string: str = f"{self.depth * ' '}{self.name}\n"

        for child in self.children:
            string += child.pprint()

        return string

    def print_leaves(self) -> str:
        """
        print_leaves Print specific for leafs

        only prints the leafs and ignores the tree structure

        Returns:
            str: underlying information of leaves
        """

        string: str = ""

        for child in self.children:
            string += child.print_leaves()

        return string

    def print_tree(self) -> str:
        """
        print_tree Print specific for leafs

        only prints the tree and ignores the leaf structure

        Returns:
            str: underlying information of leaves
        """

        string: str = f"{self.action}|{self.ccg}|{self.lx}\n"

        for child in self.children:
            string += child.print_tree()

        return string

    def print_prolog(self, depth: int = 0) -> tuple[str, int]:
        """
        print_prolog returns a string of PL format

        Using only the action, CCG and LX from tree
        using only the ccg_type, dutch_word and lemma
        to build back the PL format by using depth
        to calculate the correct amount of brackets.

        Args:
            depth (int, optional): depth, used for brackets. Defaults to 0.

        Returns:
            str: string of PL format
        """

        string: str = f"{' ' * self.depth}{self.action}({self.ccg}{', ' + self.lx if self.lx != '' else ''}"
        return_str: str

        for child in self.children:
            return_str, _ = child.print_prolog(self.depth)
            string += ",\n" + return_str

        string += ")"
        return string, depth

    def brackets_check(self, input_str: str) -> bool:
        """
        brackets_check check if the amount of brackets are logically right

        Using a stack, checks if the build with open brackets is the same as the
        debuild using closed brackets.

        Args:
            input_str (str): _description_

        Returns:
            bool: a boolean to see if the check passed
        """
        stack: list[str] = []

        for character in input_str:
            if (character == '('):
                stack.insert(0, ')')

            elif (character == '['):
                stack.insert(0, ']')

            elif (character == '<'):
                stack.insert(0, '>')

            elif (stack != [] and character == stack[0]):
                stack.pop(0)

            elif (character == ')' or character == ']' or character == '>'):
                return False

        return True

    def split_top(self, string: str, splitter: str,
                  openers: str = "([{<", closers: str = ")]}>") -> tuple[str, str]:
        ''' Splits strings at occurance of 'splitter' but only if not enclosed by brackets.
        Removes all whitespace immediately after each splitter.
        This assumes brackets, braces, and parens are properly matched - may fail otherwise
        Modified from https://stackoverflow.com/a/66699446'''

        depth: int = 0

        for counter, character in enumerate(string):
            if character in openers:
                depth += 1
            elif character in closers:
                depth -= 1

                if depth < 0:
                    raise SyntaxError()

            if not depth and character == splitter:
                return string[:counter], string[counter + 1:]

        raise Exception("This should not happen")

    def ROB(self, expr: str) -> str:
        """
        ROB Remove outer brackets

        Args:
            expr (str): input string

        Returns:
            str: string with brackets removed
        """

        if expr[0] == "(" and expr[-1] == ")":
            return expr[1: -1]
        return expr

    def parse_expression(self,
                         first: tuple[str, str],
                         second: tuple[str, str]) -> tuple[str, str]:
        # https://pure.uvt.nl/ws/portalfiles/portal/14858339/Abzianidze_Natural_20_01_2017.pdf
        # page 102
        lambda_expr: str
        new_ccg: str
        forward: Callable[[str], tuple[str, str]
                          ] = lambda x: self.split_top(x, "/")
        backward: Callable[[str], tuple[str, str]
                           ] = lambda x: self.split_top(x, "\\")

        ccg_1_front: str
        ccg_1_back: str

        ccg_2_front: str
        ccg_2_back: str

        gbc_front: str
        gbc_back: str

        direction: dict[bool, str] = {False: "/", True: "\\"}
        direction_flag: bool

        if self.action == "lx":
            if first[1] == self.lx:
                lambda_expr = f"{first[0]}"
                new_ccg = self.ccg
            else:
                print(self.action)
                print(first)
                raise ValueError("Mismatch in Lx: " +
                                 first[1] + ", is not equal with: " + self.lx)

        elif self.action in "fa":  # forward application
            lambda_expr = f"{first[0]}@{second[0]}"

            ccg_1_front, ccg_1_back = forward(first[1])

            assert self.ROB(ccg_1_back) == second[1]
            new_ccg = self.ROB(ccg_1_front)

        elif self.action in "ba":  # backward application
            lambda_expr = f"{second[0]}@{first[0]}"

            ccg_1_front, ccg_1_back = backward(second[1])

            assert self.ROB(ccg_1_back) == first[1]
            new_ccg = self.ROB(ccg_1_front)

        elif self.action in "fc":  # forward composition
            lambda_expr = f"λx.{first[0]}@({second[0]}@x)"

            ccg_1_front, ccg_1_back = forward(first[1])
            ccg_2_front, ccg_2_back = forward(second[1])

            assert ccg_1_back == ccg_2_front
            new_ccg = ccg_1_front + "/" + ccg_2_back

        elif self.action in "bc":  # backwards composition
            lambda_expr = f"λx.({second[0]})@({first[0]}@x)"

            ccg_1_front, ccg_1_back = backward(first[1])
            ccg_2_front, ccg_2_back = backward(second[1])

            assert ccg_1_front == ccg_2_back
            new_ccg = ccg_2_front + "\\" + ccg_1_back

        elif self.action in "fxc":  # forward typed composition
            lambda_expr = f"λx.({first[0]})@({second[0]}@x)"
            ccg_1_front, ccg_1_back = forward(first[1])
            ccg_2_front, ccg_2_back = backward(second[1])

            assert self.ROB(ccg_1_back) == self.ROB(ccg_2_front)
            new_ccg = ccg_1_front + "\\" + ccg_2_back

        elif self.action in "bxc":  # backward composition
            lambda_expr = f"λx.({second[0]})@({first[0]}@x)"

            ccg_1_front, ccg_1_back = forward(first[1])
            ccg_2_front, ccg_2_back = backward(second[1])

            assert ccg_1_front == ccg_2_back
            new_ccg = ccg_2_front + "/" + ccg_1_back

        elif self.action in "gfc":  # Generalized-2 forward functional composition
            lambda_expr = f"λvλu.({first[0]})@({second[0]}@v@u)"
            ccg_1_front, ccg_1_back = forward(first[1])
            try:
                ccg_2_front, ccg_2_back = backward(second[1])
                direction_flag = True
            except Exception:
                ccg_2_front, ccg_2_back = forward(second[1])
                direction_flag = False

            gbc_front, gbc_back = forward(self.ROB(ccg_2_front))

            assert self.ROB(gbc_front) == self.ROB(ccg_1_back)
            new_ccg = "(" + ccg_1_front + "/" + gbc_back + ")" + \
                direction[direction_flag] + ccg_2_back

        elif self.action in "gbc":  # Generalized-2 backward functional composition
            lambda_expr = f"λvλu.({second[0]})@({first[0]}@v@u)"

            try:
                ccg_1_front, ccg_1_back = backward(first[1])
                direction_flag = True
            except Exception:
                ccg_1_front, ccg_1_back = forward(first[1])
                direction_flag = False

            ccg_2_front, ccg_2_back = backward(second[1])

            gbc_front, gbc_back = backward(self.ROB(ccg_1_front))

            assert self.ROB(gbc_front) == self.ROB(ccg_2_back)
            new_ccg = "(" + ccg_2_front + "\\" + gbc_back + ")" + \
                direction[direction_flag] + ccg_1_back

        elif self.action in "gfxc":  # Generalized-2 forward crossing functional composition
            lambda_expr = f"λvλu.({first[0]})@({second[0]}@v@u)"
            ccg_1_front, ccg_1_back = forward(first[1])

            try:
                ccg_2_front, ccg_2_back = backward(second[1])
                direction_flag = True
            except Exception:
                ccg_2_front, ccg_2_back = forward(second[1])
                direction_flag = False

            gbc_front, gbc_back = backward(self.ROB(ccg_2_front))

            assert self.ROB(gbc_front) == self.ROB(ccg_1_back)
            new_ccg = "(" + ccg_1_front + "\\" + gbc_back + ")" + \
                direction[direction_flag] + ccg_2_back

        elif self.action in "gbxc":  # Generalized-2 backward crossing functional composition
            lambda_expr = f"λvλu.({first[0]})@({second[0]}@v@u)"

            try:
                ccg_1_front, ccg_1_back = backward(first[1])
                direction_flag = True
            except Exception:
                ccg_1_front, ccg_1_back = forward(first[1])
                direction_flag = False

            ccg_2_front, ccg_2_back = backward(second[1])

            gbc_front, gbc_back = forward(self.ROB(ccg_1_front))

            assert self.ROB(gbc_front) == self.ROB(ccg_2_back)

            new_ccg = "(" + ccg_2_front + "/" + gbc_back + ")" + \
                direction[direction_flag] + ccg_1_back

        else:
            raise NotImplementedError(
                "Not Typed Expression found: " + self.action)

        return "(" + lambda_expr + ")", new_ccg

    def return_expression(self) -> tuple[str, str]:
        second: tuple[str, str] = ("", "")

        first: tuple[str, str] = self.children[0].return_expression()

        if self.action == "ccg":
            return first

        if self.action != "lx":
            second = self.children[1].return_expression()

        output: tuple[str, str] = self.parse_expression(first, second)
        assert output[1] == self.ccg
        assert self.brackets_check(output[0])
        return output

    def __repr__(self) -> str:
        return self.pprint()
