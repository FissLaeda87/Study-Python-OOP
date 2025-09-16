class Morph:
    def __init__(self, *args):
        self.morphs = [s.lower() for s in args]

    def add_word(self, word):
        word = word.lower()
        if word not in self.morphs:
            self.morphs.append(word)

    def get_words(self):
        return tuple(self.morphs)

    def __eq__(self, other):
        if isinstance(other, str):
            word = other.lower()
            return word in self.morphs

