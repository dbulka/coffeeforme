from core.interfaces.user_interface.user_interface import UserInterface
from core.interfaces.sale_interface.sale_interface import SaleInterface
from core.interfaces.app_interface.app_interface import AppInterface
from core.controllers.sale_controller.sale_controller import SaleController


class AppController(object):
    """
    control application process
    """

    def get_saleman_id(self):
        """
        process of getting choosen saleman id
        :return: choosen saleman id
        """
        sale_interface = SaleInterface()
        get_saleman = sale_interface.get_saleman()
        if get_saleman == 'new':
            sale_controller = SaleController()
            name = input('Enter new saleman name: ')
            surname = input('Enter new saleman surname: ')
            saleman_id = sale_controller.add_new_saleman(name, surname)
            print("saleman_id: ",saleman_id)
        if get_saleman == 'exist':
            salemen_list = sale_interface.show_salemen_list()
            saleman_id = sale_interface.choose_saleman(salemen_list)
            print("saleman_id: ",saleman_id)
        return saleman_id

    def main(self):
        """
        main application process
        """
        user_interface = UserInterface()
        user_role = user_interface.select_user_role()
        print('user_role = ', user_role)
        if user_role == 'salesman':
            saleman_id = self.get_saleman_id()
            app_interface = AppInterface()
            app_interface.create_beverage()
            app_interface.get_beverage_price()


app = AppController().main()
