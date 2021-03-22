import random

while(1):
	usrNO=input("Enter a no from 1-9 or 'n' to exit")
	rand=random.randint(1,9)
	if(int(usrNO)==rand):
		print("You guessed the no right\n GUESSED NO : ",usrNO,"\nPREDICTED NO :",rand)
	elif(int(usrNO)<rand):
		print("You guessed lower \n GUESSED NO :",usrNO,"\nPREDICTED NO:",rand)
	elif(int(usrNO)>rand):
		print("You guessed higher \n GUESSED NO :",usrNO,"\nPREDICTED NO:",rand)
	else:
		break