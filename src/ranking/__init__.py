from singleton_meta import SingletonMeta
from src.player import Player


class Ranking(metaclass=SingletonMeta):
    __slots__ = ["_players"]

    def __init__(self):
        self._players = list()

    @property
    def players(self):
        return self._players

    def add_player(self, player):
        if not isinstance(player, Player):
            raise ValueError("player must be an object from class Player")
        self._players.append(player)

    def remove_player(self, player):
        try:
            self._players.remove(player)
        except ValueError:
            return False  # Correspondent Player object not found
        else:
            return True

    def del_player(self, player_nickname):
        for player in self._players:
            if player.nickname == player_nickname:
                self._players.remove(player)
                return True
        return False  # Player not found

    def get_table(self):
        if len(self._players) == 0:
            return None
        # First, sort all players by their yield coefficient
        self._players.sort(key=lambda player: player.performance.yield_coefficient, reverse=True)
        table = f"{'Nickname':<25}{'Challenges Played':<25}{'Challenges Made':<25}{'Challenge Victories':<25}" \
                f"{'Challenge Defeats':<25}{'Matches Played':<25}{'Match Victories':<25}{'Match Defeats':<25}" \
                f"Yield Coefficient\n{'-':-^224}\n"
        for player in self._players:
            table += f"{player}\n"
        return table


if __name__ == "__main__":
    rk = Ranking()
    rk.add_player(Player("leafar", "12345"))
    rk.add_player(Player("james", "54321"))
    print(rk.get_table())
