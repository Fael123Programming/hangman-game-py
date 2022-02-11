class Word:

    __slots__ = ["_word", "_hint", "_domain"]

    def __init__(self, word: str, hint: str, domain: str):
        from extra.data_persistence.database_manager import DatabaseManager
        assert domain in DatabaseManager().word_domains(), f"Domain {domain} does not exist"
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

    def __str__(self):
        data = (
            self._word,
            self._hint,
            self._domain
        )
        return data.__str__()

    @classmethod
    def instantiate(cls, word_data: tuple):
        assert len(word_data) == 3, "Word data is invalid"
        return cls(word_data[0], word_data[1], word_data[2])
