class tree_info():
    """
    tree class to parse the NLTK format into something usable
    """

    def __init__(self, left, right, label):
        self.left = left
        self.right = right
        self.label = label

    def print_lambda(self):
        left = self.left.print_lambda()
        right = self.right.print_lambda()

        if self.label == ">":
            output_str = rf"({left}@{right})"

        elif self.label == "<":
            output_str = rf"({right}@{left})"

        elif self.label == ">B":
            output_str = rf"(\x.{left}@({right}@x))"

        elif self.label == "<B":
            output_str = rf"(\x.{right}@({left}@x))"

        elif self.label == "<Bx":
            output_str = rf"(\x.{right}@({left}@x))"

        elif self.label == ">Bx":
            output_str = rf"(\x.{right}@({left}@x))"

        return output_str

    def print(self, depth=0):
        tab_str = '\t' * depth
        return f"""label: {self.label}
    {tab_str}left: {self.left.print(depth + 1)}
    {tab_str}right: {self.right.print(depth + 1)}"""

    def __repr__(self):
        return f"[left: {self.left.print()}, right: {self.right.print()}, label: {self.label}]"


class leaf_info():
    """
    leaf class to store info from the  NLTK format
    """

    def __init__(self, tree):
        self.semantics, _ = tree.label()
        for child in tree:
            for child2 in child:
                self.word = child2

    def print_lambda(self):
        return f"[{self.word}]"

    def print(self, depth=0):
        tab_str = '\t' * depth
        return f"{tab_str}Word: {self.word} & sem: {self.semantics}"

    def __repr__(self):
        return self.word
