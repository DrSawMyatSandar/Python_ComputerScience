sensor_reading = input("Enter sensor reading (dark or light): ").lower()
headlamp_switch = input("Is the headlamp switch on? (yes or no): ").lower()

# Check conditions and send signal to turn on headlamps
if sensor_reading == "dark" or headlamp_switch == "on":
    print("Sending switch-on signal to headlamps")
else:
    print("No signal")
   
