#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
import random

choice=str(input("Do you want to play Rock-Paper-Scissors\n Press y to continue \t and n to Exit\n"))


RList=["Rock","Paper","Scissor"]

while(choice!="no"):
	userVar=str(input("Enter your choice \n Rock \n Paper \n Scissor\n"))
	compVar=random.choice(RList)
	if userVar=="Rock" and compVar=="Rock":
		print("Computer : "+str(compVar)+" \nIts a TIE !!!")
	elif userVar=="Rock" and compVar=="Paper":
		print("Computer : "+str(compVar)+" \nSorry you LOSE :/")	
	elif userVar=="Rock" and compVar=="Scissor":
		print("Computer : "+str(compVar)+" \nYou WON !!!")

	elif userVar=="Paper" and compVar=="Rock":
		print("Computer : "+str(compVar)+" \nYou WON !!!")
	elif userVar=="Paper" and compVar=="Paper":
		print("Computer : "+str(compVar)+" \nIts a TIE !!!")
	elif userVar=="Paper" and compVar=="Scissor":
		print("Computer : "+str(compVar)+" \nSorry you LOSE :/")


	elif userVar=="Scissor" and compVar=="Rock":
		print("Computer : "+str(compVar)+" \nSorry you LOSE :/")
	elif userVar=="Scissor" and compVar=="Paper":
		print("Computer : "+str(compVar)+" \nYou WON !!!")
	elif userVar=="Scissor" and compVar=="Scissor":
		print("Computer : "+str(compVar)+" \nIts a TIE !!!")


	cmchoice=str(input("Do you want to play Rock-Paper-Scissors\n Press y to continue \t and n to Exit"))
	if cmchoice=="n":
		break
		

	

