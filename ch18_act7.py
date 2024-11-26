yearGroup=int(input("Enter year group"))
grade=int(input("Enter grade (9-1)"))
target=int(input("Enter target grade (9-1)"))

if yearGroup==11 and grade<target:
    print("You should attend the revision class")
else:
    print("No need to attend the revision class.")
