from core.interfaces.user_interface.user_interface import UserInterface
from core.interfaces.sale_interface.sale_interface import SaleInterface
from core.interfaces.app_interface.app_interface import AppInterface
from core.controllers.sale_controller.sale_controller import SaleController
from core.controllers.manage_controller.manage_controller import ManagerController
from utils.db_service import MySQLConnector
from mysql.connector import Error
from utils.json_writer import JSONbill
import logging


class AppController(object):
    """
    control application process
    """
    def __init__(self):
        """
        initialize new application controller
        """
        self.sale_controller = SaleController()

    def get_saleman_id(self):
        """
        process of getting choosen saleman id
        :return: choosen saleman id
        """
        sale_interface = SaleInterface()
        get_saleman = sale_interface.get_saleman()
        if get_saleman == 'new':
            name = input('Enter new saleman name: ')
            surname = input('Enter new saleman surname: ')
            saleman_id = self.sale_controller.add_new_saleman(name, surname)
            print("saleman id: ",saleman_id)
        if get_saleman == 'exist':
            salemen_list = sale_interface.show_salemen_list()
            saleman_id = sale_interface.choose_saleman(salemen_list)
        return saleman_id

    def create_order_data(self):
        """
        form data of the order
        :return: suitable data
        """
        saleman_id = self.get_saleman_id()
        app_interface = AppInterface()
        beverage = app_interface.create_beverage()
        beverage_type = beverage[0]
        ingredients = beverage[1]
        beverage_to_bill = self.sale_controller.get_beverage_types_list()[int(beverage_type[0]) - 1][1]
        ingredients_list = self.sale_controller.get_beverage_ingredients_list()
        ingredient_to_bill = []
        for ingredient in ingredients:
            ingredient_to_bill.append(ingredients_list[int(ingredient) - 1][1])
        beverage_price = app_interface.get_beverage_price()

        print("\nsaleman id #", saleman_id)
        print("beverage is ", beverage_to_bill)
        print("ingredients to bill: ", ingredient_to_bill)
        print("total price %s$" % beverage_price)
        return saleman_id, beverage_to_bill, ingredient_to_bill, beverage_price

    def write_order(self,saleman_id, price):
        """
        add order to orders table
        """
        try:
            MySQLConnector().execute_query('use coffeeforme;')
            logging.getLogger(__name__).info('use coffeeforme database')
            MySQLConnector().execute_query('insert into orders(saleman_id, price) values ("{0}","{1}");'
                                           .format(saleman_id, price))
            logging.getLogger(__name__).info('add new order(saleman_id:{0}, price:{1}$)'.format(saleman_id, price))
            MySQLConnector().execute_query('select * from orders;')
            id_order = MySQLConnector().get_results()[-1][0]
        except Error as er:
            logging.getLogger(__name__).error("Something went wrong with database %s" % er)
        return id_order


    def main(self):
        """
        main application process
        """
        user_interface = UserInterface()
        resp = True
        while resp:
            user_role = user_interface.select_user_role()
            print('user role = ', user_role)
            if user_role == 'salesman':
                order_data = self.create_order_data()
                order_id = self.write_order(order_data[0],order_data[-1])
                bill_writer = JSONbill()
                try:
                    bill_writer.write_json(order_id,order_data[0],order_data[1],order_data[2],order_data[3])
                    logging.getLogger(__name__).info('Order #%s was written'%order_id)
                except Error as er:
                    logging.getLogger(__name__).warning('Something wrong with JSON writer')
            elif user_role == 'manager':
                manager_controller = ManagerController()
                manager_controller.get_summary_of_records()
            else:
                "You haven't make choice."



