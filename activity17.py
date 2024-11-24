#activity17
marks = [[80, 59, 34, 89], [31, 11, 47, 64], [29, 56, 13, 91], [55, 61, 48, 0],[75, 78, 81, 91]]

highestMark=marks[0][0]
lowestMark=marks[0][0]

total=0
count=0

for row in marks:#80, 59, 34, 89
    for column in row:#80
        total+=column
        count+=1
        if column>highestMark:
            highestMark=column
        elif column<lowestMark:
            lowestMark=column
        
print("The highest mark is",highestMark)
print("The lowest mark is",lowestMark)
print("The average mark is",total/count)


        
    
    