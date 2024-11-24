#activity12

password=input("Enter your password")

if len(password)<6:
    print("The password you have entered is not long enough")
else:
    print("Length of password OK")


animalName = 'monkey'

for index in range(0,len(animalName)):
    print(animalName[index])
