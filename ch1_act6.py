# Assuming you have a list of existing usernames and their corresponding passwords
existing_usernames = {'user1': 'password1', 'user2':'password2'}
# Ask the user to enter their username
while True:
    username = input("Enter your username: ")
    if username in existing_usernames:
        break
    else:
        print("Username not found. Please try again.")
# Ask the user to enter their password
while True:
    password = input("Enter your password: ")
    if password == existing_usernames[username]:
        break
    else:
        print("Incorrect password. Please try again.")     
# Authentication successful
print("Login successful. Welcome,", username)
