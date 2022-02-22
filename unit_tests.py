import unittest
import sqlite3
from unittest.mock import MagicMock, Mock
from data_access import DataAccess


class UnitTests(unittest.TestCase):

    def test_sqlite3_connect_success(self):
        sqlite3.connect = MagicMock(return_value="connection succeeded", detect_types=sqlite3.PARSE_DECLTYPES)
        da = DataAccess("test_database")
        sqlite3.connect.assert_called_with("test_database", detect_types=sqlite3.PARSE_DECLTYPES)
        self.assertEqual(da.conn, "connection succeeded")

    def test_sqlite3_connect_fail(self):
        sqlite3.connect = MagicMock(return_value='connection failed', detect_types=sqlite3.PARSE_DECLTYPES)

        da = DataAccess('test_database')
        sqlite3.connect.assert_called_with('test_database', detect_types=sqlite3.PARSE_DECLTYPES)
        self.assertEqual(da.conn, 'connection failed')

    def test_db_insert_empty_obj(self):
        da = DataAccess()
        self.failureException(da.insert({}))


if __name__ == '__main__':
    unittest.main()
