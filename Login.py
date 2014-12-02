"""
Name of File: Login.py
Author: Ute Bracklow
Descr.: promt user input for login function in Zippi
"""

users={} #empty dictionary to store user data

new_user=input("Enter N for new user: ")
while new_user.upper()=="N": #loops until no new users are to be saved
    name=input("Enter your Name: ")
    password=input("Chose your Password: ")
    users[name]=password
    new_user=input("Enter N for new user: ")

login=input("Enter L for login: ")
while login.upper()=="L":
    username=input("Enter your Name: ")
    if username in users:
        userpassword=input("Enter your Password: ")
        if users[username]==userpassword:
            print("login successful")
        else:
            print("wrong password")
    else:
        print("user not found")
        login=input("Enter L for login: ")
  


        


