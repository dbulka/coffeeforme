import logging

class UserInterface(object):
    """
    interface of norole user
    """

    def select_user_role(self):
        """
        start using application from choosing  role
        :return: user role
        """
        print("""
              Welcome to CoffeeForMe - cafe managment application
                  """)
        resp = True
        responces = ('m', 's')
        while resp:
            response = input('Please choose your role: Sale or Manager. [S/M]:').lower()
            if response in responces:
                resp = False
                if response == 's':
                    user_role = 'saleman'
                else:
                    user_role = 'manager'
            else:
                print('Enter answer correctly!')
        logging.getLogger(__name__).info('User role is %s' % user_role)

ui = UserInterface()
ui.select_user_role()
