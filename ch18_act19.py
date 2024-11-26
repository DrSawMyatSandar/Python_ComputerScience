alarm = '7:30'
term_time = input('Term time?')
day = input('Day?')
if term_time == 'y' and day == 'Saturday':
    alarm = '8:00'
else:
    if term_time == 'n' or (day == 'Saturday' or day == 'Sunday'):
        alarm = '9:00'
print(alarm)
