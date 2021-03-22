happy_num=[]
def isHappy(number):
	temp=number
	Sum=int(0)
	while(temp>0):
		rem=temp%10
		Sum+=rem*rem
		temp=int(temp/10)
	return Sum
def create(Num):
	
	for i in range(1,Num+1):
		result=i
		while(result!=1 and result!=4):
			result=isHappy(result)
		if(result==1 and i not in happy_num):
			happy_num.append(i)
def writer(name):
	file_open=open(name+".txt","w+")
	file_open.write(str(happy_num)[1:-1])
	file_open.close()
	print("File successfully create :)")


# ------------main
num=int(input("Enter the range to create Happy numbers \n"))
create(num)
name=input("Enter the name for the file \n")
writer(name)