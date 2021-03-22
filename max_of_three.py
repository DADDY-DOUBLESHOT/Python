def my_max(a,b,c):
	return a if(a>b and a>c)  else b if(b>a and  b>c) else c


a,b,c=int(input("\nEnter first number\n")),int(input("\nEnter second number\n")),int(input("\nEnter third number\n"))
print("Max is ",my_max(a,b,c))