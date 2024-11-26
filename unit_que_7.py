# Display prompt and receive input from the user
weight = int(input("Enter the parcel weight (in kg):"))

# Calculate shipping cost based on the provided conditions
if weight <= 2:
    cost = 3
else:
    if weight > 10:
        cost = 3 + (8 * 2) + ((weight - 10) * 3)
    else:
        cost = 3 + ((weight - 2) * 2)

# Display the calculated cost
print("Delivery cost:", cost)
