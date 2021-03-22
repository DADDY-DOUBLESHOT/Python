

prime_num=[]

def create_list(num):
	for i in range(2,num+1):
		flag=int(0)
		for j in range(2,round(i/2)+1):
			if(i%j==0):
				flag+=1
		if(flag==0):
			prime_num.append(i)

def writer(Name):
	file_open=open(Name+".txt","w+")
	file_open.write(str(prime_num)[1:-1])
	file_open.close()
	print("File was Successfully created")


num=int(input("Enter till what to generate\n"))
create_list(num)
name=input("Enter a name for the file\n")
writer(name)
