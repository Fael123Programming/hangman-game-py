from char_analyzer import CharAnalyzer


class Match:

    __slots__ = ["_word", "_chances", "_symbols", "_player", "_hits", "_errors", "_status"]

    def __init__(self, word, chances, player):
        self._word = word  # The word to be discovered.
        self._symbols = list("*" * len(word.word))  # Represent a list of asterisks
        self._chances = chances  # Quantity of errors player may commit.
        self._player = player
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

    @property
    def player(self):
        return self._player

    def play(self):
        from src.view import View
        from time import sleep
        self._status.status = Status.in_progress()
        View.msg("Hangman Game", 50)
        print("Secret word: ", end="")
        View.print_list(self._symbols)
        print("\nErrors:", self._errors)
        print("Hint:", self._word.hint)
        View.draw_gallows(self._errors)
        while self._status.status == Status.in_progress():
            letter = input("Letter of your choice: ").lower()
            View.clean_prompt()
            analysis_result = CharAnalyzer.analyse_char(self, letter)
            View.msg(analysis_result.capitalize(), 50)
            sleep(2)
            View.clean_prompt()
            View.msg("Hangman Game", 50)
            print("Secret word: ", end="")
            View.print_list(self._symbols)
            print("\nErrors:", self._errors)
            print("Hint:", self._word.hint)
            View.draw_gallows(self._errors)
            if self._status.status == Status.victory():
                View.msg("Congratulations... You won!", 50)
            elif self._status.status == Status.defeat():
                View.msg("Oh bad... Unfortunately, you did not reach that!", 50)

    def update_status(self):
        if self._errors == self._chances:
            self._status.status = Status.defeat()
        elif self._hits == len(self._word.word):
            self._status.status = Status.victory()
        else:
            self._status.status = Status.in_progress()

    def hand_results(self):
        self._player.performance.matches_played += 1
        if self._status.status == Status.victory():  # Player won the match.
            self._player.performance.match_victories += 1
        else:
            self._player.performance.match_defeats += 1
        self._player.performance.calculate_new_yield_coe()


class Status:

    __slots__ = ["_status"]

    _DEFEAT = -1
    _VICTORY = 1
    _IN_PROGRESS = 0
    _NOT_STARTED = None

    def __init__(self):
        self._status = Status._NOT_STARTED

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status == self._DEFEAT or status == self._VICTORY or status == self._IN_PROGRESS:
            self._status = status
        else:
            raise ValueError("Unknown status")

    @classmethod
    def defeat(cls):
        return cls._DEFEAT

    @classmethod
    def victory(cls):
        return cls._VICTORY

    @classmethod
    def in_progress(cls):
        return cls._IN_PROGRESS
