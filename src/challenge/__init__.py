from match import Match
from word import Word
from player import Player


class Challenge(Match):

    __slots__ = ["_sender", "_receiver"]

    def __init__(self, word: Word, chances: int, sender: Player, receiver: Player):
        super().__init__(word, chances)
        self._sender = sender
        self._receiver = receiver

    @property
    def sender(self):
        return self._sender

    @property
    def receiver(self):
        return self._receiver
