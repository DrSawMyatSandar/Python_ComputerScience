#ch22_activity7
def read_in_data():
    rawData=open('users.txt','r')
    inputData=rawData.readlines()
    rawData.close()
    users=[]
    index=0
    for line in inputData:
        users.append(inputData[index].split(','))
        index+=1
        for names in users:
            names[1]=names[1].rstrip()
    return users

def check_user_name():
    attempt=1
    nameCorrect=False
    while attempt<4 and nameCorrect==False:
        print('\n Username attempt:',attempt)
        nameEntered=input("Enter your username:")
        valid=False
        index=0
        while valid==False and index<length:
            if users[index][0]==nameEntered:
                valid=True
            else:
                index+=1
            print(users[index][0])
            if valid==False:
                attempt+=1
            else:
                nameCorrect=True
            return index
    
def enter_password(position):
    attempt=1
    password=''
    while attempt<4 and password!=users[position][1]:
        print('\n Password attempt:',attempt)
        password=input("Enter your password:")
        if password==users[position][1]:
            print('Correct Password entered.')
        else:
            print('\nPassword incorrect')
            
#main program
users=read_in_data()
length=len(users)
positionlist=check_user_name()
print(positionlist)
if positionlist<length:
    enter_password(positionlist)
else:
    print('\nContact the system adminstrator')
