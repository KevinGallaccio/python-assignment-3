import csv
from user import User

def create_user():
    users = []
    try:
        with open ('data.txt', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                username, password, name = row
                users.append(User(username, password, name))
    except FileNotFoundError:
        print('The file "data.txt" was not found.')
    return users