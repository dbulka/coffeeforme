import configparser
import os
from enum import Enum

# CONFIG_FILE_PATH = os.path.join(os.getcwd(),'coffeeforme.ini')
CONFIG_FILE_PATH = r'C:\Users\Dell\PycharmProjects\coffeeforme\coffeeforme.ini'

class Context(object):
    """
    Contains parser methods of config from a different number of sections of CONFIG_FILE_PATH
    """

    @classmethod
    def get(cls,parameter):
        """
        Takes param from [db] section of ini file
        :param parameter:
        :return: value from a parameter as str
        """
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE_PATH)
        return config.get('config', parameter.value)

class Parameter(Enum):
    """
    Enummanation of a database confis parameters
    """
    DB_USERMANE = 'dbuser'
    DB_PASSWORD = 'dbpassword'
    DB_HOST = 'dbhost'
    DB_NAME = 'dbname'
    BASE_RESOURCE_PATH = 'base_resorce_path'

