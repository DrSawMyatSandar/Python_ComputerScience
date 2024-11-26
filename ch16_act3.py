#ch16_act3
def is_strong_password(password):
    if len(password)<8:
        return False
    has_uppercase=False
    has_special_char=False
    special_char="!@#$%^&*()_+{}[]:;<>,.?~"

    for char in password:
        if char.isupper():
            has_uppercase=True
        if char in special_char:
            has_special_char=True

    return has_uppercase and has_special_char
#main
password=input("Enter password:")
if is_strong_password(password):#True
    print("Password is strong:")
else:
    print("Password is weak:")
    
F