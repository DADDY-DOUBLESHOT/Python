import random

def check(numGuessed,theNum):
	cows=int(0)
	bulls=int(0)
	for i in range(4):
		if(numGuessed[i]==theNum[i]):
			cows+=1
		else:
			bulls+=1

	print("The Num : ",theNum,"\nGuessed num : ",numGuessed)
	print(cows," :cows",bulls," :bulls")




num=int(input("Enter a number\n"))
Rnum=int(random.randint(0000,9999))
check(str(num),str(Rnum))