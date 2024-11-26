standard_price = 5  # Replace with the actual standard price
age = int(input("Enter age:"))  # Replace with the actual age value

if age < 4:
    price = 0
else:
    if age < 16 or age > 65:
        price = standard_price / 2
    else:
        price = standard_price

# You can then use the 'price' variable as needed in the rest of your code
print(f"The calculated price is: {price}")
