import sys
def fibo(num):
	if(num==1):
		print(1)
	else:
		first=int(0)
		second=int(1)
		third=first+second
		sys.stdout.write(str(third))
		for i in range(1,num):
			sys.stdout.write("\t"+str(third))
			first=second
			second=third
			third=first+second
		print()




usr=int(input("Enter the number of length to generate : "))
fibo(usr)