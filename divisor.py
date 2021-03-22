#program which prints all the divisors for the given number

num=int(input("Enter a  number"))

Rlist=range(1,int(num/2)+1)

DList=[]
for i in Rlist:
	if num%i==0:
		DList.append(i)


print("The number "+str(num)+" can be divided by the following list")
print(DList)