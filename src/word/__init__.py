class Word:

    __slots__ = ["_word", "_hint"]

    def __init__(self, word: str, hint: str):
        self._word = word
        self._hint = hint

    @property
    def word(self):
        return self._word

    @property
    def hint(self):
        return self._hint
