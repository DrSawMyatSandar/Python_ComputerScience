#activity10
import random

play=True
correct=False

while play==True:
    randomNumber=random.randint(1,21)
    
    while correct==False:
        guess=int(input("Enter guess number:"))
        
        if guess==randomNumber:
            print("Correct")
            correct=True
            
        elif guess>randomNumber:
            print("Too High")
            
        elif guess<randomNumber:
            print("Too Low")
            
        reply=input("Do you want another?")
        if reply=='y' or reply=='Y':
            play=True
            correct=False
        else:
            play=False
                    
           
            
