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

    def add_new_saleman(self, name, surname):
        """
        add new saleman to salemen table
        :return: saleman id for control the beverage process
        """
        try:
            MySQLConnector().execute_query('use coffeeforme;')
            logging.getLogger(__name__).info('use coffeeforme database;')
            MySQLConnector().execute_query('insert into salemen(name,surname) values ("{0}","{1}");'.format(name,surname))
            logging.getLogger(__name__).info('add new salemen(name:{0}, surname:{1})'.format(name,surname))
            print('Saleman Name: {0}, Surname: {1} was created'.format(name,surname))
            MySQLConnector().execute_query('select * from salemen;')
            id_new_saleman = MySQLConnector().get_results()[-1][0]
        except Error as er:
            logging.getLogger(__name__).error("Something went wrong with database %s" % er)
        return print(id_new_saleman)

    def get_salemen_list(self):
        """
        get list of 'salemen' table (database)
        :return: salemen list
        """
        try:
            MySQLConnector().execute_query('use coffeeforme;')
            logging.getLogger(__name__).info('use coffeeforme database')
            MySQLConnector().execute_query('select * from salemen;')
            logging.getLogger(__name__).info('select all from salemen table')
        except Error as er:
            logging.getLogger(__name__).error("Something went wrong with database %s" % er)
        return MySQLConnector().get_results()

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



# name = input('name:')
# surname = input('surname:')
# sl = SaleController()
# sl.add_new_saleman(name,surname)


