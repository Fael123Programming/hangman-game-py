from data_base import DataBase


class WordProvider:

    @staticmethod
    def random_word(domain=None):
        return DataBase().get_word(domain)

