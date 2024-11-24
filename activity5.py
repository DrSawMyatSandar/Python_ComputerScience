#activity5

age=int(input("Enter your age:"))

if age<=18:
    numberLessons=20
else:
    numberLessons=20+(age-18)*2

print("You need to learn",numberLessons)



