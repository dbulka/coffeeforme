from core.interfaces.user_interface.user_interface import UserInterface
from core.interfaces.

class AppController(object):
    """
    control application process
    """

    def main(self):
        """
        main application process
        """
        user_interface = UserInterface()
        user_role = user_interface.select_user_role()
        print(user_role)
        if user_role == 'salesman':








app = AppController().main()
