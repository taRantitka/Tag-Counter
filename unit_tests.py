import unittest
from data_access import DataAccess


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.data_access = DataAccess()

    def test_db_insert(self):
        self.failureException(self.data_access.insert({}))


if __name__ == '__main__':
    unittest.main()
