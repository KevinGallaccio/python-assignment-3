class User:
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name

    def __repr__(self):
        return f'User({self.username}, {self.password}, {self.name})'