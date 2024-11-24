scores = [['Faruq',36], ['Jalila', 39], ['Isam', 48], ['Inaya', 54], ['Kadim',60],['Jumana', 69]]
#write
myfile=open("scores2.txt","w")
for index in range(len(scores)):
    myfile.write(scores[index][0]+",")
    myfile.write(str(scores[index][1])+",")
myfile.close()

#read
Blist=[]
myfile=open("scores2.txt","r")
Blist=myfile.read().split(",")
print(Blist)
myfile.close()

#2D
newList=[]
for index in range(0,len(Blist)-1,2):
    newList.append([Blist[index],Blist[index+1]])
print(newList)
