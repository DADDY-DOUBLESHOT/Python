from random import choice
import time

dump=[]


def guess(left,right):
	if(left==right):
		print("This should be the number ")
		return left
	return choice([i for i in range(left,right+1) if i not in dump])


print("Keep a number in your mind from 1-100 and let me guess it \n")
time.sleep(5)
number=int(0)

l=int(1)
r=int(100)
usrinput=0
guesses=int(0)
number=guess(l,r)
while(usrinput!=1):
	usrinput=int(input("Is "+str(number)+" the number ?\n 1:YES :) \n 2:LOWER then what i guessd :( \n 3:Higher then what i choosed :o \n"))
	if(usrinput==1):
		guesses+=1
	elif(usrinput==2):
		guesses+=1
		dump.append(number )
		l=number if l<r else l
		number=guess(l,r)
	elif(usrinput==3):
		guesses+=1
		dump.append(number)
		r=number if r>l else r
		number=guess(l,r)


print("It took ",guesses," guesses to find your number xd:")
print("\nThe numbers excluded :",dump)


