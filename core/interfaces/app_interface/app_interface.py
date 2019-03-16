from core.interfaces.sale_interface.sale_interface import SaleInterface
import logging

class AppInterface(object):
    """
    show executing by utility process
    """
    def __init__(self):
        """
        initialize new saleman inteface
        """
        self.beverage_maker = SaleInterface()

    def add_ingredients(self):
        """
        add ingredients to a beverage
        :return: additional ingredients
        """
        additianal_ingredients = []
        resp_add = True
        resp_new = True
        vars = ['y', 'n']
        while resp_add:
            while resp_new:
                responce = input('Add some ingidients? [y/n]: ').lower()
                if responce in vars:
                    resp_new = False
                else:
                    print('Enter answer correctly!')
            logging.getLogger(__name__).info('Addional ingredient = %s' % responce)
            if responce == 'y':
                beverage_ingredients_list = self.beverage_maker.show_beverage_ingredients()
                ingredient = self.beverage_maker.choose_beverage_ingredient(beverage_ingredients_list)
                additianal_ingredients += ingredient
                resp_new = True
            else:
                resp_add = False
        return additianal_ingredients

    def create_beverage(self):
        """
        show process of creating new beverage
        :return:
        """
        app = AppInterface()
        beverage_type_list = self.beverage_maker.show_beverage_type()
        beverage_type = self.beverage_maker.choose_beverage_type(beverage_type_list)
        additianal_ingredients = app.add_ingredients()

app = AppInterface()
app.create_beverage()