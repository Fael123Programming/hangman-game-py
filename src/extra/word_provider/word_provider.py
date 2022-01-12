from extra.data_persistence.database_manager import DataBaseManager
from extra.singleton_meta.singleton_meta import SingletonMeta
import sqlite3 as db


class WordProvider(metaclass=SingletonMeta):

    __slots__ = ["_database_manager", "_root_path"]

    def __init__(self, database_manager: DataBaseManager):
        from sys import path
        self._database_manager = database_manager
        self._root_path = path[1]

    @property
    def database_manager(self):
        return self._database_manager

    @property
    def root_path(self):
        return self._root_path

    def random_word(self, domain=None):
        from random import randint
        domains = self.get_all_available_domains()
        if domain is None:
            domain = domains[randint(0, len(domains) - 1)]
        else:
            valid_domain = False
            for d in domains:
                if domain == d:
                    valid_domain = True
                    break
            assert valid_domain, f"Domain {domain} does not exist"
        connection = db.connect(self._database_manager.database_path)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM words WHERE domain = {domain}")
        connection.commit()
        words_from_chosen_domain = cursor.fetchall()
        random_word = words_from_chosen_domain[randint(0, len(words_from_chosen_domain) - 1)]
        connection.close()
        return random_word

    @staticmethod
    def get_all_available_domains():
        from sys import path
        with open(path[1] + "/extra/data_persistence/domains.txt") as file:
            domains = list()
            for domain in file.readlines():
                domains.append(domain.strip())
            return domains

    def get_words_from_domain(self, domain: str):
        assert domain in self.get_all_available_domains(), f"Domain {domain} does not exist"
        connection = db.connect(self._database_manager.database_path)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM words WHERE domain = {domain}")
        words_from_chosen_domain = cursor.fetchall()
        connection.commit()
        connection.close()
        return words_from_chosen_domain
