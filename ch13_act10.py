#chapter13_activity10
message=input("Enter the message to encrypt:")
shift=int(input("Enter the size of the shift:"))

secreteMessage=""
for character in message:
    #print(character)
    number=ord(character)
    #print(number)
    if character.lower() in 'abcdefghijklmnopqrstuvwxyz':
        number+=shift
        #print(number)
        if character.isupper():
            if number>ord('Z'):
                number-=26
            elif number<ord('A'):
                number+=26
            #print(number)
        else:
            if number>ord('z'):
                number-=26
            elif number<ord('a'):
                number+=26
            #print(number)
        print(chr(number))
        secreteMessage=secreteMessage+chr(number)
        print(secreteMessage)
    else:
        secreteMessage=secreteMessage+character
        print(secreteMessage)