
import sys

  
row=int(input("Enter no of rows"))
cols=int(input("Enter no of Columns"))
i=int(0)
j=int(0)
for i in range(0,row):	
	for j in range(0,cols):
		sys.stdout.write(str(i)+str(j)+"   ")
		sys.stdout.flush()
		
	print(" ")	
	
print("Good bye -nested loop")