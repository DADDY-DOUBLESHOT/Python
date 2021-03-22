#Even odd program

num=int(input("Enter a number\n"));
if num==4:
	print("The number is a multiple of 4")

elif num%2==0:
	print("The number entered is Even")
else :
	print("The number entered is Odd")

num1=int(input("Enter first number"))
num2=int(input("Enter second number"))

if num1%num2==0:
	print("The number "+str(num1)+" was divided Evenly with "+str(num2))
