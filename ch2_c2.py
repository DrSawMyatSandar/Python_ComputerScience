import datetime
# Get current date and time
#current_time = datetime.datetime.now()
current_day = int(input("Enter day (0 to 6:Monday is 0 and Sunday is 6:)"))  # Monday is 0 and Sunday is 6
current_hour = int(input("Enter hour:"))

current_time = datetime.datetime.now()
#current_day = current_time.weekday()  # Monday is 0 and Sunday is 6
#current_hour = current_time.hour

print(type(current_time))
print(type(current_day),current_day)
print(type(current_hour),current_hour)

# Weekday temperature conditions
if 0 <= current_day <= 4:  # Monday to Friday
    if (6 <= current_hour <= 8.5) or (17.5 <= current_hour <= 22):
        temperature = 20
    else:
        temperature = None
else:  # Weekend temperature conditions
    if 8 <= current_hour <= 23:
        temperature = 22
    else:
        temperature = None

# Check for minimum temperature
if temperature is not None and temperature < 10:
    # Switch on boiler
    print("Boiler switched on!")

# Adjust temperature (this is where you would set the actual temperature in your heating system)
if temperature is not None:
    print(f"Temperature adjusted to {temperature}°C")
