#activity32
import random

number=random.randint(1,6)

guessNum=False
while guessNum==False:
    while True:
        guess=int(input("Enter guess number:"))
        if guess>0 and guess<7:
            break
    if guess==number:
        print("Well Done")
        guessNum=True
    else:
        print("Try Again")