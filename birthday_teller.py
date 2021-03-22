file1=open("birthdays.txt","r+")

file1_content=(file1.read()).split("\n")
itr=iter(file1_content)
birthdays=dict(zip(itr,itr))
print("Select the birthday of your fav scientist from below \n")
for key in birthdays:
	print(key)
scientist=input("\n")
print("\nScientist ",scientist," ",birthdays[scientist])
