from file_service import create_user

users = create_user()

def login(username, password):
    username = username.casefold()
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None