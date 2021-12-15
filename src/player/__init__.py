from match import Match, Status
from challenge import Challenge


class Player:
    __slots__ = ["_nickname", "_password", "_performance", "_challenges"]

    def __init__(self, nickname: str, password: str):
        self._nickname = nickname
        self._password = password
        self._performance = Performance()
        self._challenges = list()

    def add_challenge(self, challenge: Challenge):
        self._challenges.append(challenge)

    def remove_challenge(self, challenge: Challenge):  # If challenge is denied.
        self._challenges.remove(challenge)

    @property
    def nickname(self):
        return self._nickname

    @property
    def password(self):
        return self._password

    @property
    def performance(self):
        return self._performance

    @property
    def challenges(self):
        return self._challenges

    @nickname.setter
    def nickname(self, nickname: str):
        self._nickname = nickname

    @password.setter
    def password(self, password: str):
        self._password = password

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self._nickname == other.nickname

    def __str__(self):
        return f"{{nickname={self.nickname}, challenges_won={self.performance.challenges_won}, " \
               f"matches_won={self.performance.matches_won}, challenges_played={self.performance.challenges_played}, " \
               f"matches_played={self.performance.matches_played}, yield_coe={self.performance.yield_coefficient}}}"


class Performance:
    __slots__ = ["_challenges_played", "_matches_played", "_challenges_won", "_matches_won", "_lost_challenges",
                 "_lost_matches", "_yield_coefficient"]
    # yield = (challenges_won + matches_won) / (challenges_played + matches_played).

    def __init__(self):
        # A performance of a novice is empty.
        self._challenges_played = self._matches_played = self._challenges_won = self._matches_won = 0
        self._lost_challenges = self._lost_matches = self._yield_coefficient = 0

    @property
    def challenges_played(self):
        return self._challenges_played

    @property
    def matches_played(self):
        return self._matches_played

    @property
    def challenges_won(self):
        return self._challenges_won

    @property
    def matches_won(self):
        return self._matches_won

    @property
    def lost_challenges(self):
        return self._lost_challenges

    @property
    def lost_matches(self):
        return self._lost_matches

    @property
    def yield_coefficient(self):
        return self._yield_coefficient

    def update(self, match: Match):
        if match.__class__ == Match.__class__:  # Common match.
            self._matches_played += 1
            if match.status.status == Status.won_msg():  # Player won the match.
                self._matches_won += 1
            else:
                self._lost_matches += 1
        else:  # match is a challenge.
            self._challenges_played += 1
            if match.status.status == Status.won_msg():  # Player won the challenge.
                self._challenges_won += 1
            else:
                self._lost_challenges += 1
        self._calculate_new_yield_coe()

    def _calculate_new_yield_coe(self):
        self._yield_coefficient = (self._matches_won + self._challenges_won) / (self._matches_played +
                                                                                self._challenges_played)


if __name__ == "__main__":
    p1 = Player("rafael_king", "12345")
    print(p1)
