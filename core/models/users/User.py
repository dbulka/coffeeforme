class User(object):
    """
    parent class for all users in appication
    """

    def __init__(self, name):
        """
        initialize new user
        :param name: user's name
        """
        self.name = name