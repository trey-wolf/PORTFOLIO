correct_password = "Python123"
user_password = input("Type in your password")
if user_password == correct_password:
    print("Access Granted. Welcome to the system.")
if user_password != correct_password:
    print("Access Denied. Incorrect password.")