validNum=False
while validNum==False:
    number=int(input("Enter a number:"))
    if number>=1 and number<=10:
        validNum=True
    print("You have entered:",number)