from extra.singleton_meta.singleton_meta import SingletonMeta
from extra.data_persistence.database_manager import DataBaseManager


class Ranking(metaclass=SingletonMeta):

    @staticmethod
    def get_table():
        fields = ["nickname", "challenges_played", "challenges_made", "challenge_victories", "challenge_defeats",
                  "matches_played", "match_victories", "match_defeats", "yield_coefficient"]
        players = DataBaseManager("database").inspect_table("players", fields, "yield_coefficient", ascending=False)
        # players.sort(key=lambda pl: pl.performance.yield_coefficient, reverse=True)
        table = f"{'Nickname':<25}{'Challenges Played':<25}{'Challenges Made':<25}{'Challenge Victories':<25}" \
                f"{'Challenge Defeats':<25}{'Matches Played':<25}{'Match Victories':<25}{'Match Defeats':<25}" \
                f"Yield Coefficient\n{'-':-^224}\n"
        for player in players:
            table += f"{player[0]:<25}{player[1]:<25}{player[2]:<25}{player[3]:<25}{player[4]:<25}{player[5]:<25}" \
                     f"{player[6]:<25}{player[7]:<25}{player[8]}\n"
        return table
