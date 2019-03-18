from core.interfaces.sale_interface.sale_interface import SaleInterface, SaleController
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
        self.beverage_type_list = self.beverage_maker.show_beverage_types()
        self.beverage_type = self.beverage_maker.choose_beverage_type(self.beverage_type_list)
        logging.getLogger(__name__).info('Beverage type is #%s' %self.beverage_type)
        self.additianal_ingredients = app.add_ingredients()
        logging.getLogger(__name__).info('Additianal ingredients: %s' % self.additianal_ingredients)
        beverage_type = self.beverage_type
        additianal_ingredients = self.additianal_ingredients
        return beverage_type, additianal_ingredients

    def get_beverage_price(self):
        """
        calculating beverage price
        :return: the beverage price
        """
        beverage_type_cost = SaleController().get_beverage_types_list()[int(self.beverage_type)-1][2]
        print('beverage type cost - %s$' %beverage_type_cost)
        additional_ingredients = 0
        for ingredint in self.additianal_ingredients:
            ingredient_cost = SaleController().get_beverage_ingredients_list()[int(ingredint)-1][2]
            additional_ingredients += ingredient_cost
        print('additional ingredient cost - %s$' %additional_ingredients)
        beverage_price = beverage_type_cost + additional_ingredients
        # print('beverage cost - %s$' %beverage_price)
        logging.getLogger(__name__).info('Beverage price is %s$' %beverage_price)
        return beverage_price
