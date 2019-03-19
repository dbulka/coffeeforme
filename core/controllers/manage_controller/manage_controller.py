from utils.db_service import MySQLConnector
from mysql.connector import Error
import logging
from terminaltables import AsciiTable

class ManagerController(object):
    """
    control maganer process
    """

    def __init__(self):
        """
        initialize new ManagerController
        """
        MySQLConnector().connect()
        self.cursor = MySQLConnector().get_cursor()
        MySQLConnector().execute_query('use coffeeforme;')
        logging.getLogger(__name__).info('use coffeeforme database')

    def get_saleman_ids(self):
        """
        get list of salemen ids
        :return: list if salemen ids
        """
        saleman_ids = []
        try:
            MySQLConnector().execute_query('select id from salemen;')
            salemen = MySQLConnector().get_results()
        except Error as er:
            logging.getLogger(__name__).error("Something went wrong with database %s" % er)
        for id in salemen:
            saleman_ids.append(id[0])
        return saleman_ids

    def get_number_of_sales(self, id):
        """
        get number of sales of a saleman
        :return: number of order of a saleman
        """
        try:
            MySQLConnector().execute_query('select count(price) from orders where saleman_id = {0};'.format(id))
            saleman_number_sales = MySQLConnector().get_results()[0][0]
        except Error as er:
            logging.getLogger(__name__).error("Something went wrong with database %s" % er)
        return saleman_number_sales

    def get_total_of_saleman(self, id):
        """
        get total value of all saleman sales
        :return: total value of all saleman sales
        """
        try:
            MySQLConnector().execute_query('select sum(price) from orders where saleman_id = {0};'.format(id))
            total_saleman = MySQLConnector().get_results()[0][0]
        except Error as er:
            logging.getLogger(__name__).error("Something went wrong with database %s" % er)
        return total_saleman

    def get_seller_name(self, id):
        """
        get seleman name and surname by id
        :return: seleman name and surname by id
        """
        try:
            MySQLConnector().execute_query('select name from salemen where id = {0};'.format(id))
            name = MySQLConnector().get_results()[0][0]
            MySQLConnector().execute_query('select surname from salemen where id = {0};'.format(id))
            surname = MySQLConnector().get_results()[0][0]
            MySQLConnector().execute_query('select surname from salemen where id = {0};'.format(id))
            surname = MySQLConnector().get_results()[0][0]
            name_surname = name +', ' + surname
        except Error as er:
            logging.getLogger(__name__).error("Something went wrong with database %s" % er)
        return name_surname

    def get_seller_surname(self, id):
        """
        get seleman name and surname by id
        :return: seleman name and surname by id
        """
        try:
            MySQLConnector().execute_query('select surname from salemen where id = {0};'.format(id))
            surname = MySQLConnector().get_results()[0][0]
        except Error as er:
            logging.getLogger(__name__).error("Something went wrong with database %s" % er)
        return surname

    def get_summary_of_records(self):
        """
        show summary of all sales records
        """
        ids = self.get_saleman_ids()
        table = [
                ["Seller name","Number of sales","Total Value ($)"]
                ]
        for id in ids:
            table_id = [self.get_seller_name(id),self.get_number_of_sales(id),
                        self.get_total_of_saleman(id)]
            table.append(table_id)
        data_table = AsciiTable(table)
        print(data_table.table)

