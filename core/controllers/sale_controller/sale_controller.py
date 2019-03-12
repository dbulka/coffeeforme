from utils.db_service import MySQLConnector
from mysql.connector import Error
import logging


class SaleController(object):
    """
    controlling 'salemen' table from coffeeforme database
    """

    def __init__(self):
        """
        initialize new SaleController
        """
        MySQLConnector().connect()
        self.cursor = MySQLConnector().get_cursor()

    def get_beverage_types_list(self):
        """
        get from database list of beverage types
        :return: list beverage and cost
        """
        try:
            MySQLConnector().execute_query('use coffeeforme;')
            logging.getLogger(__name__).info('use coffeeforme database')
            MySQLConnector().execute_query('select * from beverage_types;')
            logging.getLogger(__name__).info('select all from beverage_types table')
        except Error as er:
            logging.getLogger(__name__).error("Something went wrong with database %s" % er)
        return MySQLConnector().get_results()

    def get_beverage_ingredients_list(self):
        """
        get from database list of beverage ingredients
        :return: list ingredients and cost
        """
        try:
            MySQLConnector().execute_query('use coffeeforme;')
            logging.getLogger(__name__).info('use coffeeforme database')
            MySQLConnector().execute_query('select * from beverage_ingredients;')
            logging.getLogger(__name__).info('select all from beverage_ingredients table')
        except Error as er:
            logging.getLogger(__name__).error("Something went wrong with database %s" % er)
        return MySQLConnector().get_results()


# cl = SaleController()
# print(cl.get_beverage_ingredients_list())


