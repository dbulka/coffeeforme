from core.controllers.sale_controller.sale_controller import SaleController
import logging


class SaleInterface(object):
    """
    user interface of saleman
    """

    def show_salemen_list(self):
        """
        show salemen list
        :return: salemen list
        """
        salemen_list = SaleController().get_salemen_list()
        salemen_numbers = []
        print("""
                      Please choose a saleman:
                      """)
        for saleman in salemen_list:
            print('id #{0} - {1} {2}'.format(saleman[0], saleman[1], saleman[2]))
        for i in range(len(salemen_list)):
            salemen_numbers.append(i + 1)
        return salemen_numbers

    def choose_saleman(self, salemen_numbers):
        """
        choose salemen
        :return: saleman id for control the beverage process
        """
        resp = True
        while resp:
            choosen_saleman = input('Please enter id number of saleman: #')
            try:
                if int(choosen_saleman) in salemen_numbers:
                    resp = False
                else:
                    print('Enter number attentive!')
            except:
                print('Enter number attentive!')
        logging.getLogger(__name__).info('Saleman id %s was choose ' % choosen_saleman)
        return choosen_saleman

    def get_saleman(self):
        """
        choose way "add new saleman" or "get existing"
        """
        resp = True
        while resp:
            print('Do you want add new saleman or get existing?')
            responce = input('Enter \'new\' or \'exist\' :')
            if responce == 'new':
                resp = False
            elif responce == 'exist':
                resp = False
            else:
                print('Please enter answer correctly.')
        return responce

    def show_beverage_types(self):
        """
        show beverage types
        :return: beverage types
        """
        beverage_type_list = SaleController().get_beverage_types_list()
        type_numbers = []
        print("""
              Please choose beverage type:
              """)
        for beverage_type in beverage_type_list:
            print('#{0} {1} {2}$'.format(beverage_type[0],beverage_type[1],beverage_type[2]))
        for i in range(len(beverage_type_list)):
            type_numbers.append(i+1)
        return type_numbers

    def choose_beverage_type(self, type_numbers):
        """
        choose beverage type
        :return: choosen beverage
        """
        resp = True
        while resp:
            choosen_beverage = input('Please enter number of beverage type: #')
            try:
                if int(choosen_beverage) in type_numbers:
                    resp = False
                else:
                    print('Enter number attentive!')
            except:
                print('Enter number attentive!')
        logging.getLogger(__name__).info('Bavarage type %s was choose ' %choosen_beverage)
        return choosen_beverage

    def show_beverage_ingredients(self):
        """
        show beverage ingredients
        :return: show beverage ingredients
        """
        beverage_ingredients_list = SaleController().get_beverage_ingredients_list()
        ingredients_numbers = []
        print("""
              Please choose additional ingredient:
              """)
        for ingredient in beverage_ingredients_list:
            print('#{0} {1} {2}$'.format(ingredient[0],ingredient[1],ingredient[2]))
        for i in range(len(beverage_ingredients_list)):
            ingredients_numbers.append(i+1)
        return ingredients_numbers

    def choose_beverage_ingredient(self, ingredients_numbers):
        """
        choose beverage ingredient
        :return: choosen beverage ingredient
        """
        resp = True
        while resp:
            choosen_ingredient = input('Please enter number of beverage ingredient #')
            try:
                if int(choosen_ingredient) in ingredients_numbers:
                    resp = False
                else:
                    print('Enter number correctly!')
            except:
                print('Enter number correctly!')
        logging.getLogger(__name__).info('Bavarage ingredient %s was choose ' %choosen_ingredient)
        return choosen_ingredient

