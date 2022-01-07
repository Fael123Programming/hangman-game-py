from src.singleton_meta import SingletonMeta


class DataBase(metaclass=SingletonMeta):

    @staticmethod
    def get_word(domain):
        if domain is None:
            return "Word from no specific domain"
        else:
            return "Word from " + domain  # If domain is a valid domain!
