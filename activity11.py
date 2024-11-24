#activity11

anotherGo="y"
while anotherGo=="y" or anotherGo=="Y":
    
    while True:
        choice=input("Select an option: a-addition,s-subtraction,m-multiplication,d-division:")
        
        if choice=="a" or choice=="s" or choice=="d" or choice=="m":
            break
        
        else:
            print("Invalid")
        
    firstNumber=int(input("Enter first number:"))
    secondNumber=int(input("Enter second number:"))
        
    if choice=="a":
        print(firstNumber+secondNumber)
        
    elif choice=="s":
        print(firstNumber-secondNumber)
            
    elif choice=="m":
        print(firstNumber*secondNumber)
            
    else:
        print(firstNumber/secondNumber)

    anotherGo=input("Do you want another go (y or n)?")