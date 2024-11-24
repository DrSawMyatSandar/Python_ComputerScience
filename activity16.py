#activity16
firstNames=['Ashura', 'Bryn', 'Eloise', 'Mei', 'James', 'Irena']

searchName=input("Enter search name")
found=False
index=0

while found==False and index<=len(firstNames)-1:
    if searchName==firstNames[index]:
        found=True
    index=index+1
        
if found==True:
    print(searchName,"is at position",index,"in the list")
else:
    print(searchName,"is not in the list")
        