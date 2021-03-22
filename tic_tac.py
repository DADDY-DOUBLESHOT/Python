


def check(player,board):

	flag=int(0)

	for i in range(0,3):
		row=set([board[i][0],board[i][1],board[i][2]])
		if(next(iter(row))==player and board[i][0]!=0) and len(row)==1:
			flag+=1
			print("flag :",flag,"row :",row)
			return bool(1)
			break
	for i in range(0,3):
		cols=set([board[0][i],board[1][i],board[2][i]])
		if(next(iter(cols))==player and board[0][i]!=0) and len(cols)==1:
			flag+=1
			print("flag :",flag,"cols :",cols)
			return bool(1)
			break
	diag1=set([board[0][0],board[1][1],board[2][2]])
	diag2=set([board[0][2],board[1][1],board[2][0]])
	flag = 1 if (next(iter(diag1))==player and len(diag1)==1) or (next(iter(diag2))==player and len(diag2)==1) else 0

	print("flag :",flag,"diag 1:",diag1,"diag2 :",diag2)
	
	return bool(1) if flag==1 else bool(0)










# --------------------------main------------------------
first=[]
second=[]
third=[]
print("Enter first Row\n")
for i in range(3):
	temp=int(input())
	first.append(temp)
print("Enter Second Row\n")
for i in range(3):
	temp=int(input())
	second.append(temp)
print("Enter third Row\n")
for i in range(3):
	temp=int(input())
	third.append(temp)
list=[first,second,third]

print("Checking for the winners....")
player_one=int(1)
player_two=int(2)

print(list)

# print("player one: ",(check(player_one,list)))
# print("player two: ",(check(player_two,list)))

if(check(player_one,list) and not(check(player_two,list))):
	print("Player one Won")
elif(check(player_two,list) and not(check(player_one,list))):
	print("Player two Won")
elif(check(player_one,list) and check(player_two,list)):
	print("Its a fucking tie..")
elif(not(check(player_one,list)) and not(check(player_two,list))):
	print("No one  Wins")