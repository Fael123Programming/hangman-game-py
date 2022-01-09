from extra.singleton_meta.singleton_meta import SingletonMeta
import sqlite3 as db


class DataBaseManager(metaclass=SingletonMeta):
    __slots__ = ["_database_name"]  # No attributes for an instance of this class

    def __init__(self, database_name: str):
        assert len(database_name) > 0 and database_name.isalpha(), f"Database name {database_name} is invalid!"
        self._database_name = database_name + ".db"
        connection = db.connect(self._database_name)  # Creates the .db file
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
        connection = db.connect(self._database_name)
        cursor = connection.cursor()
        cursor.execute(f"CREATE TABLE {name} ({fields_str})")
        connection.commit()
        connection.close()

    def insert_data(self, table_name: str, data: tuple):
        connection = db.connect(self._database_name)
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {table_name} VALUES {data}")
        connection.commit()
        connection.close()

    def inspect_table(self, table_name: str, fields: str | list, rows=-1):
        assert fields == "*" or isinstance(fields, list) and len(fields) > 0, "Fields argument is invalid!"
        connection = db.connect(self._database_name)
        cursor = connection.cursor()
        if fields == "*":
            cursor.execute(f"SELECT * FROM {table_name}")
        else:
            fields_str = ""
            counter = 1
            for field in fields:
                fields_str += field
                if counter < len(fields):
                    fields_str += ", "
                counter += 1
            cursor.execute(f"SELECT {fields_str} FROM {table_name}")
        if rows <= 0:  # Then, get all rows!
            required_data = cursor.fetchall()
        else:
            required_data = cursor.fetchmany(rows)
        return required_data

    @property
    def database_name(self):
        return self._database_name
