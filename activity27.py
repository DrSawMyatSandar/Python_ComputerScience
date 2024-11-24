def newUser():
    print("New user")
def login():
    print("login")
def changePassword():
    print("change password")

print ( "1. Register as a new user") 
print ( "2. Login.") 
print ( "3. Change your password.") 
print ( "4. Exit.") 

correct=0
while correct==0:
    choice = int(input('Please select a menu option.')) 
    
    if choice == 1:
        newUser()
        correct=1
    elif choice==2:
        login()
        correct=1
    elif choice == 3:
        changePassword()
        correct=1
    elif choice == 4: 
        exit()
        correct=1
    else:
        print('Incorrect option. Try again.')
