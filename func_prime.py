#Ask the user for a number and determine whether the number is prime or not

def func_prime(Unum):
	count =int("0")
	ListA= range(2,int(Unum/2)+1)
	for i in ListA:
		if Unum%i==0:
			count=count+1
	if count==0:
		print("Its a Prime Number")
	else :
		print("Its not a Prime Number")




#main prog

num=int(input("Enter a number..."))
func_prime(num)




			


