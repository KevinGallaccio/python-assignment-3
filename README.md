# Assignment 3 - User Validation with CSV File in Python

## **Overview**
This project is a Python implementation of **Assignment #3** from Coders Campus, which involves validating user login credentials by reading from a CSV file. The original assignment was written in Java, and I translated it into Python while ensuring it maintained the same behavior.

---

## **Original Java Assignment Instructions**

### **Objective**
Create a **user login system** where users input their **username and password**, and the program validates them against stored credentials from a file (`data.txt`).

### **Requirements**
1. **Store user information** in a file (`data.txt`) and read it into the application.
2. **Create a `User` object** with three properties:
   - `username`
   - `password`
   - `name`
3. **Read data from the file into an array of `User` objects`**.
4. **Prompt the user for login credentials** using `Scanner` (Java) or `input()` (Python).
5. **Validate credentials:**
   - **Username is case-insensitive**.
   - **Password is case-sensitive**.
6. **Login Flow:**
   - If the credentials match, display: `Welcome {User's Name}` and exit.
   - If incorrect, prompt again (up to **5 attempts**).
   - If the user fails after 5 attempts, display: `Too many failed login attempts, you are now locked out.` and exit.

### **Matching Rules**
✅ **Valid match:**
```plaintext
Input:  TREVOR@CRAFTYCODR.COM
Stored: trevor@craftycodr.com
✅ MATCH
```
❌ **Invalid match:**
```plaintext
Input:  trevor.page@craftycodr.com
Stored: trevor@craftycodr.com
❌ NO MATCH
```
✅ **Valid password match:**
```plaintext
Input:  test123
Stored: test123
✅ MATCH
```
❌ **Invalid password match:**
```plaintext
Input:  Test123
Stored: test123
❌ NO MATCH
```

### **Sample Output**
#### **Use Case #1: Too Many Failed Logins**
```plaintext
Enter your email:
test@test.com
Enter your password:
asdfasdf
Invalid login, please try again
...
Too many failed login attempts, you are now locked out.
```
#### **Use Case #2: Successful Login**
```plaintext
Enter your email:
john.doe@mydomain.net
Enter your password:
Hdk398jf!
Welcome: John Doe
```

---

## **Translating This to Python**
### **Challenges & Lessons Learned**

### **1️⃣ Java’s `Scanner` vs. Python’s `input()`**
- Java requires `Scanner` to read user input.
- Python’s `input()` handles it more concisely:
  ```python
  username = input("Enter your username: ")
  ```

### **2️⃣ Reading CSV File Instead of `data.txt`**
- In Java, we might use a `BufferedReader` to read a text file.
- In Python, `csv.reader` makes this process cleaner:
  ```python
  with open('data.txt', mode='r') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
          users.append(User(row[0], row[1], row[2]))
  ```

### **3️⃣ Case-Insensitive Username Matching**
- Java might use `.equalsIgnoreCase()`, but in Python, we use `.casefold()`:
  ```python
  username.casefold() == user.username.casefold()
  ```

---

## **Python Implementation**

### **`user.py`** (User Data Model)
```python
class User:
    def __init__(self, username, password, name):
        self.username = username.casefold()
        self.password = password
        self.name = name

    def __repr__(self):
        return f'User({self.username}, {self.password}, {self.name})'
```

### **`file_service.py`** (Loading Users from File)
```python
import csv
from user import User

def create_user():
    users = []
    try:
        with open ('data.txt', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                users.append(User(row[0], row[1], row[2]))
    except FileNotFoundError:
        print('The file "data.txt" was not found.')
    return users
```

### **`user_service.py`** (Authentication Logic)
```python
from file_service import create_user

users = create_user()

def login(username, password):
    username = username.casefold()
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None
```

### **`login_service.py`** (Handling Login Attempts)
```python
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
```

### **`main.py`** (Entry Point)
```python
from login_service import login_app

if __name__ == "__main__":
    login_app()
```

---

## **Conclusion**
✅ Successfully implemented a **user authentication system in Python** that mimics the Java version.  
✅ Learned key differences between **file handling, case sensitivity, and input validation** in Java vs. Python.  
✅ **Python’s `casefold()` makes case-insensitive comparisons cleaner than Java’s `.equalsIgnoreCase()`.**  

**Next steps:** Improve error handling, add password hashing for security, and implement a **better user management system!** 🚀🐍

---

**🛠️ Built With:**
- Python 3
- No external libraries (pure Python implementation)

📌 **Author:** Kevin Gallaccio[https://github.com/KevinGallaccio]
📌 **Based On:** Coders Campus[https://coderscampus.com/]

🚀 **Excited for the next assignment!**

