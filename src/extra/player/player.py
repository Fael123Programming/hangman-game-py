from extra.challenge.challenge import Challenge
from extra.player.performance import Performance


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

    def tuple(self):
        data = (
            self._nickname,
            self._password,
            self.performance.matches_played,
            self.performance.match_victories,
            self.performance.match_defeats,
            self.performance.challenges_played,
            self.performance.challenge_victories,
            self.performance.challenge_defeats,
            self.performance.challenges_made,
            self.performance.yield_coefficient
        )
        return data

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self._nickname == other.nickname

    def __str__(self):
        data = (
            self._nickname,
            self._password,
            self.performance.matches_played,
            self.performance.match_victories,
            self.performance.match_defeats,
            self.performance.challenges_played,
            self.performance.challenge_victories,
            self.performance.challenge_defeats,
            self.performance.challenges_made,
            self.performance.yield_coefficient
        )
        return data.__str__()

    def __repr__(self):
        return repr((self._nickname, self._password))
