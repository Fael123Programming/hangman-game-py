from extra.singleton_meta.singleton_meta import SingletonMeta
from extra.player.player import Player
import sqlite3 as db


class DatabaseManager(metaclass=SingletonMeta):
    __slots__ = ["_database_name", "_database_path"]  # No attributes for an instance of this class

    def __init__(self, database_name="database"):
        from sys import path
        assert len(database_name) > 0 and database_name.isalpha(), f"Database name {database_name} is invalid!"
        self._database_name = database_name + ".db"
        self._database_path = path[1] + f"/extra/data_persistence/{database_name}.db"
        connection = db.connect(self._database_path)  # Creates the .db file
        connection.close()  # Closes its stream

    def create_table(self, name: str, fields: dict):
        fields_str = ""  # To contain a string with all fields and their respective data types organized.
        # Example: let fields = {"name": "text", "age": "integer"}, then fields_str would be "name text, age integer".
        counter = 1
        for field_name, data_type in fields.items():
            fields_str += f"{field_name} {data_type}"
            if counter < len(fields):
                fields_str += ", "
            counter += 1
        connection = db.connect(self._database_path)
        cursor = connection.cursor()
        cursor.execute(f"CREATE TABLE {name} ({fields_str})")
        connection.commit()
        connection.close()

    def delete_table(self, table: str):
        connection = db.connect(self._database_path)
        cursor = connection.cursor()
        cursor.execute(f"DROP TABLE {table}")
        connection.commit()
        connection.close()

    def insert_data(self, table_name: str, data: str):
        # data must be a string representation of a tuple of values
        # according to the fields of the table.
        connection = db.connect(self._database_path)
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {table_name} VALUES {data}")
        connection.commit()
        connection.close()

    def inspect_table(self, table_name: str, fields: str | list, field_conditions: None | dict, sorting_field: str,
                      ascending=True, rows=-1):
        assert fields == "*" or isinstance(fields, list) and len(fields) > 0, f"Fields argument {fields} is invalid!"
        connection = db.connect(self._database_path)
        cursor = connection.cursor()
        fields_str = fields
        if isinstance(fields, list):
            fields_str = self._stringify(fields)
        sorting_mode = "DESC" if not ascending else "ASC"
        if field_conditions is None:
            cursor.execute(f"SELECT {fields_str} FROM {table_name} ORDER BY {sorting_field} {sorting_mode}")
        else:
            assert isinstance(field_conditions, dict), "Field conditions must be None or a dict"
            field_conditions_str = self._stringify_logic(field_conditions)
            cursor.execute(f"SELECT {fields_str} FROM {table_name} WHERE {field_conditions_str} ORDER BY "
                           f"{sorting_field} {sorting_mode}")
            connection.commit()
        table_data = cursor.fetchall() if rows <= 0 else cursor.fetchmany(rows)
        connection.close()
        return table_data

    def get_players_for_ranking(self):
        connection = db.connect(self._database_path)
        cursor = connection.cursor()
        fields = ["nickname", "challenges_played", "challenges_made", "challenge_victories", "challenge_defeats",
                  "matches_played", "match_victories", "match_defeats", "yield_coefficient"]
        cursor.execute(f"SELECT {self._stringify(fields)} FROM players ORDER BY yield_coefficient DESC LIMIT 1000")
        connection.commit()
        players = cursor.fetchall()
        connection.close()
        return players

    def update_record(self, table_name: str, field_values: dict, field_conditions: dict):
        field_values_str = self._stringify_comma(field_values)
        field_conditions_str = self._stringify_logic(field_conditions)
        connection = db.connect(self._database_path)
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {table_name} SET {field_values_str} WHERE {field_conditions_str}")
        connection.commit()
        connection.close()

    def delete_record(self, table_name: str, field_conditions: dict):
        field_conditions_str = self._stringify_logic(field_conditions)
        connection = db.connect(self._database_path)
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE {field_conditions_str}")
        connection.commit()
        connection.close()

    def select_player(self, nickname: str):
        assert not nickname.isspace() and len(nickname) > 0, "Invalid nickname"
        connection = db.connect(self._database_path)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM players WHERE nickname = '{nickname}'")
        connection.commit()
        player_data = cursor.fetchone()
        if player_data is None:  # No player found with the specified nickname at all
            return player_data
        return Player.instantiate(player_data)

    def domains(self) -> list:
        connection = db.connect(self._database_path)
        cursor = connection.cursor()
        cursor.execute("SELECT domain_name FROM domains ORDER BY domain_name ASC")
        connection.commit()
        domains = list()
        for domain_tuple in cursor.fetchall():
            domains.append(domain_tuple[0])
        return domains

    def words_from_domain(self, domain: str):
        assert domain in self.domains(), f"Domain {domain} does not exist"
        connection = db.connect(self._database_path)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM words WHERE domain = '{domain}' ORDER BY word")
        connection.commit()
        words = cursor.fetchall()
        connection.close()
        return words

    def challenges_of_player(self, player_nickname: str) -> list | None:
        player = self.select_player(player_nickname)
        if player is None:
            return player
        from extra.challenge.challenge import Challenge
        challenges_list = self.inspect_table("challenges", "*", {"receiver_nickname": player_nickname}, "word")
        for counter in range(len(challenges_list)):
            challenges_list[counter] = Challenge.instantiate(challenges_list[counter])
        return challenges_list

    @property
    def database_name(self):
        return self._database_name

    @property
    def database_path(self):
        return self._database_path

    @staticmethod
    def _stringify_comma(a_dict: dict) -> str:
        result = ""
        counter = 1
        for key, value in a_dict.items():
            result += key + " = "
            if isinstance(value, str):
                result += f"'{value}'"
            else:
                result += str(value)
            if counter < len(a_dict):
                result += f", "
            counter += 1
        return result

    @staticmethod
    def _stringify_logic(a_dict: dict) -> str:
        result = ""
        counter = 1
        for key, value in a_dict.items():
            result += key + " = "
            if isinstance(value, str):
                result += f"'{value}'"
            else:
                result += str(value)
            if counter < len(a_dict):
                result += f" AND "
            counter += 1
        return result

    @staticmethod
    def _stringify(a_list: list):
        result = ""
        for counter in range(len(a_list)):
            result += str(a_list[counter])
            if counter < len(a_list) - 1:
                result += ", "
        return result
