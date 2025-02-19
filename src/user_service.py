from file_service import create_user

users = create_user()

def login(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return user
    else:
        return None