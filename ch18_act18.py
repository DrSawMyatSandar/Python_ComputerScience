colour=input("Enter colour: ")  
size =input("Enter size: ")  
leaves=input("Enter leaves condition (cracked/misshapen/other):")  
leaftips=input("Enter leave tips (True or False:)")
advice = 'nothing'  # Default advice

if colour == 'yellow':
    if leaftips == 'True':
        advice = 'magnesium'
    else:
        advice = 'nitrogen'
elif colour == 'brown':
    if size == 'small':
        advice = 'phosphorous'
    elif size == 'normal':
        advice = 'potassium'
else:
    if leaves == 'cracked' or leaves == 'misshapen':
        advice = 'calcium'

print("Advice:", advice)
