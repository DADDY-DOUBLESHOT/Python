#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions

def funct_fibo(length):
	n1=0
	n2=1
	i=0
	while i<length:
		n3=n1+n2
		print(n3)
		n1=n2
		n2=n3
		i=i+1

#main prog

length=int(input("How many numbers to print..?"))
funct_fibo(length)
	
	