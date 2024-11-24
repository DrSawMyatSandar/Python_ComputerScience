albumCollection = [['Where Rivers Meet', 'Z Rahman', 2008, 'World'], ['Best of Cat Stevens', 'C Stevens', 1984, 'Pop'],
                   ['Come Away With Me', 'N Jones', 2012, 'Pop'],['Shine', 'Bond', 2002, 'Instrumental'],
                   ['Blessing', 'J Rutter', 2012, 'Classical']]

anotherGo="y"
while anotherGo=="y" or anotherGo=="Y":
    while True:
        choice=input("Press e to enter details of a new album, or s to search for an album.")
        if choice=="e" or choice=="s":
            break
    if choice=="e":
            #enter
        newAlblum=[]
            
        album=input("Enter your album:")
        artist=input("Enter your artist:")
        year=int(input("Enter release year:"))
        genre=input("Enter genre:")
            
        newAlblum=[album,artist,year,genre]
        albumCollection.append(newAlblum)
    else:
        #search
        searchAblum=input("Enter search album name:")
        
        found=False
        index=0
        while found==False and index<len(albumCollection):
            if albumCollection[index][0]==searchAblum:
                found=True
                print("Artist:",albumCollection[index][1],"\nYear of Release",albumCollection[index][2])
            else:
                index=index+1
        if found==False:
            print("This album is not in the list:")
    anotherGo=input("Press y if you want another go")