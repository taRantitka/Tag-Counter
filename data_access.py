import sqlite3
import logging
import pickle


class DataAccess:
    DEFAULT_DB_NAME = "tag_counter.db"
    DEFAULT_GENERATOR_NAME = "db_generator.sql"

    def __init__(self, db_name=DEFAULT_DB_NAME):
        sqlite3.register_converter("pickle", pickle.loads)
        sqlite3.register_adapter(list, pickle.dumps)
        self.conn = sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES)

    def generate(self, generator_name=DEFAULT_GENERATOR_NAME):
        try:
            cursor = self.conn.cursor()

            with open(generator_name, 'r') as sqlite_file:
                sql_script = sqlite_file.read()

            cursor.execute(sql_script)
            logging.info("Database successfully created.")
            cursor.close()

        except sqlite3.Error as error:
            logging.exception(error)
        finally:
            self.conn.close()
            logging.info("Connection closed.")

    def insert(self, obj):
        try:
            logging.info(f"{obj} is inserting to database...")

            with self.conn:
                self.conn.execute(
                    "INSERT INTO reports VALUES (?, ?, ?, ?)",
                    obj
                )

        except sqlite3.Error as error:
            logging.exception(error)

    def get(self, site_name):
        try:
            data = self.conn.execute(
                'SELECT site_name, url, check_date, report as "report [pickle]" FROM reports WHERE site_name=?',
                (site_name,)).fetchone()

            logging.info(f"Data retrieved from database.")

            return data
        except sqlite3.Error as error:
            logging.exception(error)


