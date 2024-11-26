# Assuming testScore is a variable that holds the student's test score
testScore = float(input("Enter the test score: "))

# Determine the grade based on the test score
if testScore >= 80:
    grade = 'A'
elif testScore >= 70:
    grade = 'B'
elif testScore >= 60:
    grade = 'C'
elif testScore > 0:
    grade = 'D'
else:
    grade = 'FAIL'

# Display the calculated grade
print("Grade:", grade)

0