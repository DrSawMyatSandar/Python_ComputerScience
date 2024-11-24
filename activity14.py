#activity14

firstName=input("Enter first name:")
lastName=input("Enter last name:")

length=len(lastName)

if length==1:
    lastName=lastName+"XXX"

elif length==2:
    lastName=lastName+"XX"

elif length==3:
    lastName=lastName+"X"

userName=lastName[0:4]+firstName[0]
print("Your user name is:",userName)
