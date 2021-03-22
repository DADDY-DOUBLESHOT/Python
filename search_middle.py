



def middleout(left,right,num,list):
	
	middle=int(round((left+right)/2))

	

	if(list[len(list)-1]<num):
		print("The number is not present")
	elif(left==right or left>right):
		print("The number is not present")
	elif(list[middle]==num):
		print("The number is present")
	elif(num>list[middle]):
		lft=middle
		rght=right
		middleout(lft,rght,num,list)
	elif(num<list[middle]):
		lft=left
		rght=middle
		middleout(lft,rght,num,list)








def search(num,list):
	middleout(0,len(list),num,list)
	

alist=[]
length=int(input("How many numbers you want to enter"))
for i in range(length):
	temp=int(input())
	alist.append(temp)
alist.sort()
num=int(input("Enter a number to search\n"))
search(num,alist)