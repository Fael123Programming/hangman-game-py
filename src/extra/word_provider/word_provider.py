from extra.data_persistence.database_manager import DatabaseManager
from extra.singleton_meta.singleton_meta import SingletonMeta


class WordProvider(metaclass=SingletonMeta):

    __slots__ = ["_database_manager"]

    def __init__(self, database_manager: DatabaseManager):
        self._database_manager = database_manager

    @property
    def database_manager(self):
        return self._database_manager

    def random_word(self, domain=None):
        from random import randint
        from extra.word.word import Word
        domains = self._database_manager.word_domains()
        if domain is None:
            domain = domains[randint(0, len(domains) - 1)]  # Random domain!
        else:
            valid_domain = False
            for d in domains:
                if domain == d:
                    valid_domain = True
                    break
            assert valid_domain, f"Domain {domain} does not exist"
        words_list = self._database_manager.words_from_domain(domain)
        random_word_tuple = words_list[randint(0, len(words_list) - 1)]
        return Word.instantiate(random_word_tuple)
