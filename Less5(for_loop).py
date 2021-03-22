#program to print numbers from list < 5

List = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
slist=[]

print("The entire List is "+str(List));
print("Elements less then 5 are as follows");
for i in List:

	if i<5:
	

		print(str(i)+"\n");
		slist.append(i);

	
print("Separate List is as follows "+str(slist))


var=int(input("Enter a number "))
print("Elements less then "+str(var)+" are as follows");
for i in List:
	if i<var:
		print(i)
