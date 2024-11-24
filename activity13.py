#activity13

string='The cars present included Ford, Mercedes, Toyota, BMW, Audi and Renault'
car=input("Enter your search car:")

string=string.upper()
car=car.upper()

if car in string:
    print('It is present')
else:
    print('It is not present')
