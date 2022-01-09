from extra.match.match import Match
from extra.match.status import Status


class Challenge(Match):
    __slots__ = ["_sender"]

    def __init__(self, word, chances, receiver, sender):
        super().__init__(word, chances, receiver)  # receiver is the player.
        self._sender = sender

    @property
    def sender(self):
        return self._sender

    # Overridden method!
    def hand_results(self):
        self._sender.performance.challenges_made += 1
        self.player.performance.challenges_played += 1
        if self.status.status == Status.victory():
            self._sender.performance.challenge_defeats += 1
            self.player.performance.challenge_victories += 1
        else:
            self._sender.performance.challenge_victories += 1
            self.player.performance.challenge_defeats += 1
        self._sender.performance.calculate_new_yield_coe()
        self.player.performance.calculate_new_yield_coe()
