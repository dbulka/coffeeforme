from core.interfaces.user_interface.user_interface import UserInterface
from core.interfaces.sale_interface.sale_interface import SaleInterface
from core.interfaces.app_interface.app_interface import AppInterface
from core.controllers.sale_controller.sale_controller import SaleController


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
            print("saleman_id: ",saleman_id)
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


    def main(self):
        """
        main application process
        """
        user_interface = UserInterface()
        user_role = user_interface.select_user_role()
        print('user_role = ', user_role)
        if user_role == 'salesman':
            self.create_order_data()


app = AppController().main()
