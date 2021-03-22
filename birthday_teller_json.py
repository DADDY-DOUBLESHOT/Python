import json

file=open("Birthdays.json","r")
content=json.load(file)
print("Enter any Scientist name from below to know his birthday")
for i in content:
	print(i)
scientist=input("\n")
print("Scientist ",scientist,content[scientist])