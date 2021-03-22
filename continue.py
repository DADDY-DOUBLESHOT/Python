num=int(input("Enter a number to skip"))
i=int(0)
for i in range(0,100):
	if (i==num):
		continue
	print(i)
print("Good bye -continue")