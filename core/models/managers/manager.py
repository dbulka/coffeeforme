from core.models.users.User import User


class Manager(User):
    """
    'manager' user position class
    """

    def show_summary(self):
        """
        show summary of all the sales records
        :return: table with "seller name", "number of sales", "total values"
        """
        pass