from user_service import login

def login_app():
    login_attempts = 0
    max_login_attempts = 5
    while login_attempts < max_login_attempts:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user = login(username, password)
        if user:
            print(f"Welcome, {user.name}!")
            return
        else:
            print("Invalid username or password. Please try again.")
            login_attempts += 1
    print("Too many failed attempts. You've been locked out.")