# Receive height from the user
height = float(input("Enter your height (in inches):"))

# Receive weight from the user
weight = float(input("Enter your weight (in lb):"))

# Calculate BMI (Body Mass Index)
bmi = 703*weight / (height ** 2)
# Display the calculated BMI
print("Your BMI is:", bmi)
