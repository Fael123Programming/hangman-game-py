class Word:

    __slots__ = ["_word", "_hint", "_domain"]

    def __init__(self, word: str, hint: str, domain: str):
        self._word = word
        self._hint = hint
        self._domain = domain

    @property
    def word(self):
        return self._word

    @property
    def hint(self):
        return self._hint

    @property
    def domain(self):
        return self._domain
