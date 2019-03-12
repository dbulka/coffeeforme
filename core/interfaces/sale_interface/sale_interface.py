from core.controllers.sale_controller.sale_controller import SaleController
import logging


class SaleInterface(object):
    """
    user interface of saleman
    """

    def show_beverage_type(self):
        """
        show beverage type
        :return: show beverage
        """
        beverage_type_list = SaleController().get_beverage_types_list()
        type_numbers = []
        print("""
              Please choose your beverage type:
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
            choice = input('Please enter number of beverage type #')
            try:
                if int(choice) in type_numbers:
                    resp = False
                else:
                    print('Enter number attentive!')
            except:
                print('Enter number attentive!')
        logging.getLogger(__name__).info('Bavarage type %s was choose ' %choice)
        return choice

sm = SaleInterface()
gb = sm.show_beverage_type()
sm.choose_beverage_type(gb)