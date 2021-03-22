
def check(num):
	if(num==1):
		return int(1)
	i=int(0)
	for i in range(2,num):
		if(num%i==0):
			return int(0)
			break
	return int(1)

usr=int(input("Enter a Number : "))
if(check(usr)==1):
	print(check(usr))
	print("Its a prime number")
else:
	print("Its not a prime")