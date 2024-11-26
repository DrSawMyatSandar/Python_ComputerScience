attempts = 0

while attempts < 3:
    # Prompt the user to enter the PIN
    
    pin = int(input("Enter PIN:"))

    # Check if the entered PIN is correct
    if pin == 111:
        print("Approve Payment")
        break  # Exit the loop if the PIN is correct
    else:
        attempts += 1
        print(f"Incorrect PIN. {3 - attempts} attempts remaining.")

# Check if the maximum attempts are reached
if attempts == 3:
    print("Lock Card")
