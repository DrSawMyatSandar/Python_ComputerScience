charge=0
total=0
number=0
anotherGo="y"
while anotherGo=="Y" or anotherGo=="y":
    charge=10
    number=number+1
    age=int(input("Enter customer age:"))
    
    if age<13:
        charge=5
        number=number-1
    elif age>=60:
        charge=9
    total=total+charge
    print(total)
    anotherGo=input("Another member y or n:")
    
if number>4:
    total=total-10
    print(total)
else:
    print(total)
