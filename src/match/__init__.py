from word import Word


class Match:

    __slots__ = ["_word", "_chances", "_symbols", "_hits", "_errors", "_status"]

    def __init__(self, word: Word, chances: int):
        self._word = word  # The word to be discovered.
        self._symbols = list("*" * len(word.word))  # Represent a list of asterisks
        self._chances = chances  # Quantity of errors player may commit.
        self._hits = 0  # Quantity of hit.
        self._errors = 0  # Quantity of mistakes.
        self._status = Status()  # Match status.

    @property
    def word(self):
        return self._word

    @property
    def chances(self):
        return self._chances

    @property
    def hits(self):
        return self._hits

    @property
    def errors(self):
        return self._errors

    @property
    def symbols(self):
        return self._symbols

    @property
    def status(self):
        return self._status

    def _analyse_char(self, char: str) -> str:
        if len(char) > 1:
            self._errors += 1
            return "mais que um caractere digitado"
        elif len(char) == 0:
            self._errors += 1
            return "nenhum caractere digitado"
        elif not char.isalpha():
            self._errors += 1
            return "caractere invalido"
        else:
            hit = False
            for letter in range(len(self._word.word)):
                if self._word.word[letter] == char:
                    self._symbols[letter] = char
                    self._hits += 1
                    hit = True
            if not hit:
                self._errors += 1
            return "caractere encontrado" if hit else "caractere nao encontrado"

    def play(self):
        from src.view import System
        from time import sleep
        System.msg("Hangman Game", 50)
        print("Secret word: ", end="")
        System.print_list(self._symbols)
        print("\nErrors:", self._errors)
        print("Hint:", self._word.hint)
        System.draw_gallows(self._errors)
        won = lose = False
        while True:
            letter = input("Letter of your choice: ").lower()
            System.clean_prompt()
            res = self._analyse_char(letter)
            won, lose = res == Status.won_msg(), res == Status.lose_msg()
            System.msg(res.capitalize(), 50)
            sleep(2)
            System.clean_prompt()
            System.msg("Hangman Game", 50)
            print("Secret word: ", end="")
            System.print_list(self._symbols)
            print("\nErrors:", self._errors)
            print("Hint:", self._word.hint)
            System.draw_gallows(self._errors)
            if won or lose:
                return self


class Status:
    """
   Esta classe representa o status atual de uma partida e é utilizada para a contabilidade do desempenho
   do jogador ao final da partida.
   O status de uma partida pode ser:
   - Se o número de erros cometidos pelo jogador é igual à quantidade de chances: "jogador perdeu";
   - Senão se os acertos conseguidos pelo jogador são iguais ao tamanho de palavra secreta: "jogador venceu";
   - Senão, o status será: "em andamento".
   """
    __slots__ = ["_status"]

    _LOSE = "jogador perdeu"
    _WON = "jogador venceu"
    _IN_PROGRESS = "em andamento"

    def __init__(self):
        self._status = Status._IN_PROGRESS

    def update_status(self, match: Match):
        if match.errors == match.chances:
            self._status = Status._LOSE
        elif match.hits == len(match.word.word):
            self._status = Status._WON
        else:
            self._status = Status._IN_PROGRESS

    @property
    def status(self):
        return self._status

    @classmethod
    def lose_msg(cls):
        return cls._LOSE

    @classmethod
    def won_msg(cls):
        return cls._WON

    @classmethod
    def in_progress_msg(cls):
        return cls._IN_PROGRESS
