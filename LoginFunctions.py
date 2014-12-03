"""
Name of File: Login.py
Author: Ute Bracklow
Descr.: promt user input for login function in Zippi
"""

users={} #empty dictionary to store user data

def addNewUser():   #function to add new users
    name=input("Enter your Name: ")
    password=input("Chose your Password: ")
    users[name]=password
    print("User saved as ", name, "with password ", password)
    main()          #to "loop" until q is entered 
    
def userLogin():    #funtion to promt login data and excecute login
    username=input("Enter your Name: ")
    if username in users:
        userpassword=input("Enter your Password: ")
        if users[username]==userpassword:
            print("login successful")
        else:
            print("wrong password")
            main()  #to "loop" until q is entered 
    else:
        print("user not found")
        main()      #to "loop" until q is entered 

def main(): 
    choice=input("Enter N for new user, L for Login, Q to exit: ")
    if choice.upper()=="N":
        addNewUser()
    elif choice.upper()=="L":
        userLogin()
    elif choice.upper()=="Q":
        print("You wish to exit. See you!")
    else:
        print("Not a valid choice.")

main()

    


    


        


