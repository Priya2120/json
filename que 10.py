import json

def login(usr):
    a = input("Name: ")
    s = input("Password: ")

    if a in usr.keys():
        if s == usr[a]:
            print("Welcome back.")
        else:
            print("Incorrect password.")
            return False
    else:
        print("Hello, new person.")
        usr[a] = s

    writeUsers(usr)
    return True

def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def writeUsers(usr):
    with open("users.json", "w+") as f:
            json.dump(usr, f)

users = readUsers()
success = login(users)

while not success:
    success = login(users)