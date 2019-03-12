import mysql.connector
from mysql.connector import Error
import logging
from utils.context import Context, Parameter


class DBConnector(object):
    """
    An interface for various DB connectors
    """

    def connect(self, *args, **kwargs):
        """ Retrieves an db connection """

    def get_cursor(self, *args, **kwargs):
        """ Returns an cursor object which able to execute queries"""

    def execute_query(self, *args, **kwargs):
        """ Executes an query for connection db"""

    def shutdown(self):
        """Close cursor and connection"""

class MySQLConnector(DBConnector):
    """
    Connector for exection common MySQL database methods
    """
    INSTANCE = None
    connection = None
    cursor = None

    def __new__(cls):
        """
        A singleton implementation for mysql connector
        :return: MySQLConnector instance
        """
        if not cls.INSTANCE:
            cls.INSTANCE = super().__new__(cls)
        return cls.INSTANCE

    def connect(self):
        """
        Implements connection params from config, creates mysql db connection
        """
        try:
            self.connection = mysql.connector.connect(host=Context.get(Parameter.DB_HOST),
                                                      database=Context.get(Parameter.DB_NAME),
                                                      user=Context.get(Parameter.DB_USERMANE),
                                                      password=Context.get(Parameter.DB_PASSWORD),
                                                      auth_plugin='mysql_native_password')
            self.connection.autocommit = True
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                logging.getLogger(__name__).info("Connected to MySQL Server version on %s" %db_info)
        except Error as er:
            logging.getLogger(__name__).error("Error while connecting to MySQL %s" %er)

    def get_cursor(self):
        """
        Retrieves an cursor object for DB-API interaction
        :return: cursor object or none if we got exception
        """
        try:
            self.cursor = self.connection.cursor()
            logging.getLogger(__name__).info("Cursor was created.")
        except Error as er:
            logging.getLogger(__name__).error("Something went wrong with cursor creating. %s" %er)
        finally:
            return self.cursor

    def get_results(self):
        return self.cursor.fetchall()

    def execute_query(self, query):
        """
        :param query: str object like sql query
        :return: rusults of query as typle or none if we got exception
        """
        try:
            query = self.cursor.execute(query)
            logging.getLogger(__name__).info("Query was execute.")
        except Error as er:
            logging.getLogger(__name__).error("Error while executing query %s" %er)

    def shutdown(self):
        """
        close the connection
        """
        try:
            if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                logging.getLogger(__name__).info("Connection was succesfully closed.")
            logging.getLogger(__name__).info("Connection already closed.")
        except Error as er:
            logging.getLogger(__name__).error("Error while closing channel %s" %er)

# conn = MySQLConnector()
# conn.connect()
# conn.get_cursor()
# conn.execute_query('select * from beverage_type;')
# conn.execute_query('select * from beverage_type;')
# print(conn.get_results())


