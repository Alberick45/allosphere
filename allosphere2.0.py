from Entry import *
from retrieval import retrieval
admin_username = {"albert": "pass5", "terry": "pass4", "chris": "pass2"}
name = input("Enter your name")
print("hello " + name)
if name.lower() not in admin_username:
    print("sorry you must be an admin to continue")
    exit()
else:
    password = input("type your password")
    trial = 1
    if trial <= 2 and password == admin_username[name]:
        print(name + " has been successfully logged in")
    else:
        trial += 1
        print("sorry try again")
        password = input("type your password")
        if password == admin_username[name]:
            print(name + " has been successfully logged in")
        else:
            print("sorry try again later")
            exit()

proceed = "yes"
while proceed == "yes":
    user_action = input("What would you like to do? (entry/retrieve) ")
    if user_action == "entry":
        entry()
    elif user_action == "retrieve":
        retrieval()
    else:
        print("Option not recognized. Please choose 'entry' or 'retrieve'.")
    proceed = input("Would you like to continue? (yes/no) ").lower()
