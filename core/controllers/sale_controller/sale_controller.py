from utils.db_service import MySQLConnector
import sqlalchemy


class SaleController(object):
    """
    controlling 'salemen' table from coffeeforme database
    """

    def __init__(self):
        """
        initialize new SaleController
        """
        MySQLConnector().connect()
        # self.cursor = MySQLConnector().get_cursor()

    def show_salemen(self):
        """
        show 'salemen' table
        :return: table of salemen and ids
        """
        metadata = sqlalchemy.MetaData()
        for t in metadata.sorted_tables:
            print(t.name)


cl = SaleController()
cl.show_salemen()
