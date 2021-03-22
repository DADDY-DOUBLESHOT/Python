#program that returns a list that contains only the elements that are common between the lists (without duplicates)
import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common=[]

for i in a:
	if (i in b) and i not in common :
		common.append(i)
print("Elements which were common are as follows "+str(common))

print("Now generating a random list\n")

randm=[]
for i in range(0,50):
	randm.append(random.randint(0,100))
print(randm)
