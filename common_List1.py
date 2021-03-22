a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# a=[1,1,1,1,1,2]
# b=[1,1,1,1,3]
common=[]
c=[]
d=[]
if(len(a)>len(b)):
	c=a
	d=b
else:
	c=b
	d=a

for i in c:
	if i in d and i not in common:
		common.append(i)

print("Common elements :\t ",common)

