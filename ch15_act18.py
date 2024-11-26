#ch15_activity18
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS=LETTERS.lower()
def encrypt(message,key):#hello,3
    encrypted=""
    for chars in message:
        if chars in LETTERS:
            num=LETTERS.find(chars)#h=7
            num+=key#7+3=10 ==k
            encrypted+=LETTERS[num]
    return encrypted  
def decrypt(message,key):#khoor
    decrypted=""
    for chars in message:
        if chars in LETTERS:
            num=LETTERS.find(chars)#k
            num-=key
            decrypted+=LETTERS[num]
    return decrypted
def main():
    message=input("Enter your message:")
    key=int(input("Enter your key 1-26:"))
    choice=input("Encrypt or Decrypt (e or d):")
    if choice.lower().startswith('e'):
        print(encrypt(message,key))
    else:
        print(decrypt(message,key))
#main
main()           
