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
        while resp:
            response = input('Please write your role - Salesman or Manager : ').lower()
            if response == 'manager':
                resp = False
            elif response == 'salesman':
                resp = False
            else:
                print('Enter answer correctly!')
        logging.getLogger(__name__).info('User role is %s' % response)
        return response


