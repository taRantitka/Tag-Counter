import sqlite3


class DbCreator:
    DEFAULT_DB_NAME = "tag_counter.db"
    DEFAULT_GENERATOR_NAME = "db_generator.sql"

    @staticmethod
    def generate(db_name=DEFAULT_DB_NAME,
                 generator_name=DEFAULT_GENERATOR_NAME):
        try:
            sqlite_connection = sqlite3.connect(db_name)
            cursor = sqlite_connection.cursor()

            with open(generator_name, 'r') as sqlite_file:
                sql_script = sqlite_file.read()

            cursor.execute(sql_script)
            print("Database successfully created.")
            cursor.close()

        except sqlite3.Error as error:
            print(error)
        finally:
            if (sqlite_connection):
                sqlite_connection.close()
                print("Connection closed.")
