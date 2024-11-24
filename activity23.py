postCode=input("Enter a post code:")

#length=len(postCode)

if len(postCode)>=6 and len(postCode)<=8:
    print("Valid")
else:
    print("Invalid")