from utils.db_service import MySQLConnector
from mysql.connector import Error
import unittest


class TestDB(unittest.TestCase):

    def test_add_new_saleman(self):
        """
        Test that last record to salemen table is new saleman
        """
        name = 'Tomara'
        surname = 'Dream'
        MySQLConnector().connect()
        self.cursor = MySQLConnector().get_cursor()
        MySQLConnector().execute_query('use coffeeforme;')
        MySQLConnector().execute_query('insert into salemen(name,surname) values ("{0}","{1}");'
                                           .format(name, surname))
        MySQLConnector().execute_query('select * from salemen;')
        last_saleman = MySQLConnector().get_results()[-1]
        self.assertIn(name, last_saleman)
        self.assertIn(surname, last_saleman)

if __name__ == '__main__':
    unittest.main()
