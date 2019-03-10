from core.models.users.User import User

class Saleman(User):
    """
    'saleman' user position class
    """

    def choose_beverage_type(self):
        """
        choose beverage type
        :return: choosen beverage
        """
        pass

    def add_ingredients(self):
        """
        choose ingredients type
        :return: choosen ingredients
        """
        pass

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

    