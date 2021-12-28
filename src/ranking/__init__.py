from singleton_meta import SingletonMeta
from sorting_object import DualPivotQuickSort


class Ranking(metaclass=SingletonMeta):

    __slots__ = ["_players"]

    def __init__(self):
        self._players = list()

    @property
    def players(self):
        DualPivotQuickSort().sort(self._players)
        return self._players

    def addPlayer(self, player):
        self._players.append(player)

    def removePlayer(self, player):
        try:
            self._players.remove(player)
        except ValueError:
            return False
        else:
            return True

    def delPlayer(self, player_nickname):
        for player in self._players:
            if hasattr(player, "nickname"):
                if player.nickname == player_nickname:
                    self._players.remove(player)
                    return True
        return False
