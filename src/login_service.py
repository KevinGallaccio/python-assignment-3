from user_service import login

def login_attempt():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return login(username, password)

def login_app():
    for attempt in range(5):
        user = login_attempt()
        if user:
            print(f"Welcome, {user.name}!")
            return
        print("Invalid username or password. Please try again.")
    print("Too many failed attempts. You've been locked out.")