from extra.singleton_meta.singleton_meta import SingletonMeta
from extra.data_persistence.database_manager import DatabaseManager


class Ranking(metaclass=SingletonMeta):

    @staticmethod
    def get_table():
        fields = ["nickname", "challenges_played", "challenges_made", "challenge_victories", "challenge_defeats",
                  "matches_played", "match_victories", "match_defeats", "yield_coefficient"]
        players = DatabaseManager("database").inspect_table("players", fields, "yield_coefficient", ascending=False,
                                                            field_conditions=None)
        # players.sort(key=lambda pl: pl.performance.yield_coefficient, reverse=True)
        size = 20
        table = f"{'Nickname':<{size}}{'Challenges Played':<{size}}{'Challenges Made':<{size}}{'Challenge Victories':<{size}}" \
                f"{'Challenge Defeats':<{size}}{'Matches Played':<{size}}{'Match Victories':<{size}}{'Match Defeats':<{size}}" \
                f"Yield Coefficient\n{'-':-^180}\n"
        for player in players:
            table += f"{player[0]:<{size}}{player[1]:<{size}}{player[2]:<{size}}{player[3]:<{size}}{player[4]:<{size}}{player[5]:<{size}}" \
                     f"{player[6]:<{size}}{player[7]:<{size}}{player[8]}\n"
        return table.strip()
