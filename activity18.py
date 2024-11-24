#activity18
gameScores = [['Alexis', 1, 19], ['Seema', 1, 29], ['Seema', 2, 44], ['Lois', 1,10], ['Alexis', 2, 17], ['Alexis', 3, 36], ['Dion', 1, 23], ['Emma', 1, 27], ['Emma', 2, 48]]
highestL1Score=0
highestL1Player=""

highestL2Score=0
highestL2Player=""

highestL3Score=0
highestL3Player=""

for row in gameScores:#'Alexis', 1, 19
    player=row[0]
    level=row[1]
    score=row[2]
    
    if level==1 and score>highestL1Score:
        highestL1Score=score
        highestL1Player=player
    elif level==2 and score>highestL2Score:
        highestL2Score=score
        highestL2Player=player
    elif level==3 and score>highestL3Score:
        highestL3Score=score
        highestL3Player=player
  
print('The highest score in Level 1 was', highestL1Score, 'achieved by', highestL1Player)
print('The highest score in Level 2 was', highestL2Score, 'achieved by', highestL2Player)
print('The highest score in Level 3 was', highestL3Score, 'achieved by', highestL3Player)
