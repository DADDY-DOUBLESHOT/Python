import random

tank=['Rock','Paper','Scissor']
comp=int(int(tank.index(random.choice(tank)))+1)
usr=int(input("Select from \n1: Rock \n2: Paper \n3: Scissor\n"))
if(comp==usr):
	print("Computer : ",tank[comp-1],"\nUser : ",tank[usr-1])
	print("Its a tie")
elif(comp==1 and usr==3):
	print("Computer : ",tank[comp-1],"\nUser : ",tank[usr-1])
	print("You won")
elif(comp<usr):
	print("Computer : ",tank[comp-1],"\nUser : ",tank[usr-1])
	print("You Won")
else:
	print("Computer : ",tank[comp-1],"\nUser : ",tank[usr-1])
	print("You Lose")
