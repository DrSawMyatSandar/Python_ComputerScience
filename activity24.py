scores = [36, 39, 48, 54, 60]
myfile=open("scores.txt","w")
for index in range(len(scores)):
    myfile.write(str(scores[index])+",")
myfile.close()

#read
newScores=[]
myfile=open("scores.txt","r")
newScores=myfile.read().split(",")
print(newScores)
myfile.close()