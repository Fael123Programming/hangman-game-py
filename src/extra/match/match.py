from extra.char_analyzer.char_analyzer import CharAnalyzer
from extra.match.status import Status
from extra.data_persistence.database_manager import DataBaseManager
from extra.player.player import Player


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
        from extra.view.view import view
        self._status.status = Status.in_progress()
        view = view()
        ch_an = CharAnalyzer()
        view.msg("Hangman Game")
        print("Secret word: ", end="")
        view.print_list(self._symbols)
        print("\nErrors:", self._errors)
        print("Hint:", self._word.hint)
        view.draw_gallows(self._errors)
        while self._status.status == Status.in_progress():
            letter = input("Letter of your choice: ").lower()
            view.clean_prompt()
            analysis_result = ch_an.analyse_char(self, letter)
            view.msg(analysis_result.capitalize())
            view.stop()
            view.clean_prompt()
            view.msg("Hangman Game")
            print("Secret word: ", end="")
            view.print_list(self._symbols)
            print("\nErrors:", self._errors)
            print("Hint:", self._word.hint)
            view.draw_gallows(self._errors)
            if self._status.status == Status.victory():
                view.msg("Congratulations... You won!")
                view.stop(2)
            elif self._status.status == Status.defeat():
                view.msg("Oh bad... Unfortunately, you did not reach that!")
                view.stop(2)
            view.clean_prompt()

    def update_status(self):
        if self._errors == self._chances:
            self._status.status = Status.defeat()
        elif self._hits == len(self._word.word):
            self._status.status = Status.victory()
        else:
            self._status.status = Status.in_progress()

    def hand_results(self):
        assert isinstance(self._player, Player), f"Player {self._player} cannot receive results"
        self._player.performance.matches_played += 1
        if self._status.status == Status.victory():  # Player won the match.
            self._player.performance.match_victories += 1
        else:
            self._player.performance.match_defeats += 1
        self._player.performance.calculate_new_yield_coe()
        player_data = {
                "matches_played": self._player.performance.matches_played,
                "match_victories": self._player.performance.match_victories,
                "match_defeats": self._player.performance.match_defeats,
                "yield_coefficient": self._player.performance.yield_coefficient
        }
        DataBaseManager("database").update_record("players", player_data, {"nickname": self._player.nickname})
