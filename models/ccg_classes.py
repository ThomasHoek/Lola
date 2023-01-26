
class leaf_info():
    def __init__(self, tree):
        self.semantics, _ =  tree.label()
        for child in tree:
            for child2  in child:
                self.word = child2

    def print(self):
        return f"Word: {self.word} & sem: {self.semantics}"

    def __repr__(self):
        return self.word