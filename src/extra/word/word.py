from extra.word_provider.word_provider import WordProvider


class Word:

    __slots__ = ["_word", "_hint", "_domain"]

    def __init__(self, word: str, hint: str, domain: str):
        assert word.isalpha(), f"Word {word} is invalid!"
        assert hint.isalpha(), f"Hint {hint} is invalid!"
        assert domain in WordProvider().get_all_available_domains(), f"Domain {domain} does not exist"
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
