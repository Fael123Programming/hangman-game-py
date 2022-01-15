from extra.match.status import Status


class Match:
    from extra.word.word import Word
    from extra.player.player import Player

    __slots__ = ["_word", "_chances", "_symbols", "_player", "_hits", "_errors", "_status"]

    def __init__(self, word: Word, player: Player, chances=5):
        from extra.match.status import Status
        self._word = word  # The word to be discovered.
        self._symbols = self.get_asterisks(word)  # Represent a list of asterisks
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

    @hits.setter
    def hits(self, hits: int):
        assert hits >= 0, f"Hits {hits} must be non-negative"
        self._hits = hits

    @errors.setter
    def errors(self, errors: int):
        assert errors >= 0, f"Errors {errors} must be non-negative"
        self._errors = errors

    def play(self):
        from extra.view.view import View
        from extra.char_analyzer.char_analyzer import CharAnalyzer
        self._status.status = Status.in_progress()
        view = View()
        ch_an = CharAnalyzer()
        while self._status.status == Status.in_progress():
            view.msg("Hangman Game")
            print("Secret word:", view.stringify_list(self.symbols))
            print("Hits:", self._hits)
            print("Errors:", self._errors)
            print("Hint:", self._word.hint)
            if self._player != "None":
                print("Player:", self._player.nickname)
            view.row()
            view.draw_gallows(self._errors)
            view.row()
            letter = input("Letter of your choice: ").lower()
            view.clean_prompt()
            analysis_result = ch_an.analyse_char(self, letter)
            view.msg(analysis_result.capitalize())
            view.stop()
            view.clean_prompt()
            if self._status.status == Status.victory():
                view.msg("Congratulations... You won!")
                view.stop(2)
            elif self._status.status == Status.defeat():
                view.msg("Oh bad... Unfortunately, you did not reach that!")
                view.stop(2)
        view.clean_prompt()
        if self._player != "None":
            self.hand_results()

    def update_status(self):
        if self._errors == self._chances:
            self._status.status = Status.defeat()
        elif self._hits == len(self._word.word):
            self._status.status = Status.victory()
        else:
            self._status.status = Status.in_progress()

    def hand_results(self):
        from extra.player.player import Player
        from extra.data_persistence.database_manager import DatabaseManager
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
        DatabaseManager().update_record("players", player_data, {"nickname": self._player.nickname})

    @staticmethod
    def get_asterisks(word: Word) -> list:
        result = list()
        for char in word.word:
            if not char.isspace():
                result.append("*")
            else:
                result.append(char)
        return result
