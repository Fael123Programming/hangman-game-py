from extra.singleton_meta.singleton_meta import SingletonMeta


class Ranking(metaclass=SingletonMeta):

    @staticmethod
    def get_table():
        players = list()  # Receives all players from database
        players.sort(key=lambda pl: pl.performance.yield_coefficient, reverse=True)
        table = f"{'Nickname':<25}{'Challenges Played':<25}{'Challenges Made':<25}{'Challenge Victories':<25}" \
                f"{'Challenge Defeats':<25}{'Matches Played':<25}{'Match Victories':<25}{'Match Defeats':<25}" \
                f"Yield Coefficient\n{'-':-^224}\n"
        for player in players:
            table += f"{player}\n"
        return table
