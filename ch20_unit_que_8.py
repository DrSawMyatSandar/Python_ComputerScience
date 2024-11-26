S = int(input("Enter street sensor (0 or 1):"))
B = int(input("Enter building sensor (0 or 1):"))
M = int(input("Enter manual switch sensor (0 or 1):"))

if (S == 1 or B == 1) and M == 0:
    
    command_to_send = 'open'
    print(f"Sending {command_to_send} to door_opening_mechanism")
