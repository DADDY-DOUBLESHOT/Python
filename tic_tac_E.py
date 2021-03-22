import random
import os

global list



def create_board():
	return [[0,0,0],[0,0,0],[0,0,0]]
def mark(x,y,player,list):
	list[x][y]=player.upper()


def show(list):
	print("")
	for i in range(3):
		for j in range(3):
			print(list[i][j],end=" ")
		print("")
			
			



def check(player):
	# ----------------rows------------------
	for i in range(3):
		row=set([list[i][0],list[i][1],list[i][2]])
		if(len(row)==1 and str(next(iter(row))).upper()==str(player).upper() and next(iter(row))!=0):
			return bool(1)
	# ------------------cols-----------------
	for i in range(3):
		col=set([list[0][i],list[1][i],list[2][i]])
		if(len(col)==1 and str(next(iter(col))).upper()==str(player).upper() and next(iter(col))!=0):
			return bool(1)
	# -----------------diagnoals-----------------
	diag1=set([list[0][0],list[1][1],list[2][2]])
	diag2=set([list[0][2],list[1][1],list[2][0]])
	if((len(diag1)==1 or len(diag2)==1) and (next(iter(diag1))==str(player).upper() or next(iter(diag2))==str(player).upper())):
		return bool(1)
	else:
		return bool(0)



def change(player):
	return  1 if player==2 else 2



def screen_clear():
	os.system("clear")




# -------------------main---------------------


list=create_board();
player1=(input("\nChoose for Player one\n"))
player2=(input("\nChoose for Player two\n"))
players=[1,2]
who=random.choice(players)
# character='X' if who==
for i in range(9):
	print("Mark your Co-ordinates Player ",who)
	x,y=int(input()),int(input())
	mark(x,y,(player1 if who==1 else player2),list)
	show(list)
	if(check(player1 if who==1  else player2)):
		screen_clear()
		print("\nPlayer  ",who," won \n")
		show(list)
		break
	who=change(who)

if(not(check('x'))and not(check('o'))):
	print("No one wins")






