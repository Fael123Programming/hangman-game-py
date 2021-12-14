class Word:

    def __init__(self, word: str, hint: str):
        self.__word = word
        self.__hint = hint

    @property
    def word(self):
        return self.__word

    @property
    def hint(self):
        return self.__hint