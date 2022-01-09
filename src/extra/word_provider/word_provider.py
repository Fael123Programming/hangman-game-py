from extra.data_persistence.database_manager import DataBaseManager
from extra.singleton_meta.singleton_meta import SingletonMeta
import sqlite3 as db


class WordProvider(metaclass=SingletonMeta):

    __slots__ = ["_database_manager"]

    def __init__(self, database_manager: DataBaseManager):
        self._database_manager = database_manager

    @property
    def database_manager(self):
        return self._database_manager

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
        connection = db.connect("../data_persistence/" + self._database_manager.database_name)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM words WHERE domain = {domain}")
        words_from_chosen_domain = cursor.fetchall()
        random_word = words_from_chosen_domain[randint(0, len(words_from_chosen_domain) - 1)]
        connection.commit()
        connection.close()
        return random_word

    @staticmethod
    def get_all_available_domains():
        with open("../data_persistence.domains.txt") as file:
            domains = list()
            for domain in file.readlines():
                domains.append(domain.strip())
            return domains

    def get_words_from_domain(self, domain: str):
        assert domain in self.get_all_available_domains(), f"Domain {domain} does not exist"
        connection = db.connect("../data_persistence/" + self._database_manager.database_name)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM words WHERE domain = {domain}")
        words_from_chosen_domain = cursor.fetchall()
        connection.commit()
        connection.close()
        return words_from_chosen_domain
