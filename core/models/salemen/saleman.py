from core.models.users.User import User
from core.controllers.sale_controller.sale_controller import SaleController

class Saleman(User):
    """
    'saleman' user position class
    """

    def add_ingredients(self, choice):
        """
        choose ingredients type
        :return: choosen ingredients
        """


    def get_beverage_price(self):
        """
        calculating beverage price
        :return: beverage price
        """
        pass

    def save_order_in_bill(self):
        """
        save bill(file) with sale details
        :return:
        """
        pass

    def save_order_in_database(self):
        """
        save sale details in database
        :return:
        """
        pass

# sm = Saleman('John')
# sm.show_beverage_type()