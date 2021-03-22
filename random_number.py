#Program to Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
dec=""
guess=int("0")

while(1>0):


	num=int(input("Enter a number from 1 to 9\n"))
	guess=guess+1

	Rnum=random.randint(1,9)
	if num==Rnum:

		print("You Guessed the Number right \nRandom number :"+str(Rnum)+"\nYour Number :"+str(num))

	elif num<Rnum:

		print("Your Guessed number was less then the Random Number \nRandom number :"+str(Rnum)+"\nYour Number :"+str(num))

	elif num>Rnum:

		print("Your Guessed number was Greater then the Random Number \nRandom number :"+str(Rnum)+"\nYour Number :"+str(num))


	dec=input("Press Enter to continue else type exit to terminate")
	if dec=="exit":
		print("You took total guesses of "+str(guess))
		quit()

