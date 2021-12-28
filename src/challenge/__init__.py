from match import Match
from match import Status


class Challenge(Match):

    __slots__ = ["_sender"]

    def __init__(self, word, chances, receiver, sender):
        super().__init__(word, chances, receiver)
        self._sender = sender

    @property
    def sender(self):
        return self._sender

    def hand_results(self):
        self._sender.performance.challenges_made += 1
        self._player.performance.challenges_played += 1
        if self._status.status == Status.VICTORY():
            self._sender.performance.challenge_defeats += 1
            self._player.performance.challenge_victories += 1
        else:
            self._sender.performance.challenge_victories += 1
            self._player.performance.challenge_defeats += 1
        self._sender.performance.calculate_new_yield_coe()
        self._player.performance.calculate_new_yield_coe()
