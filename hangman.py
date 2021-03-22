str1="FRIZLIER"
size=int(len(str1))








def display(indexs,string):
	for i in range(len(string)):
		if(i in show_pos):
			print(string[i],end=" ")
		else:
			print("_",end=" ")



def find_index(guess,string):
	for i in range(len(string)):
		if(guess==string[i]):
			return i









show_pos=[0,size-1,round((size)/2)]

print("Guess the letters for ")
display(show_pos,str1)
for i in range(7):
	guess=input("\nenter your guess\n")
	if(guess in str1):
		show_pos.append(find_index(guess,str1))
		display(show_pos,str1)
	else:
		print("\nNope\n")

	
	


if(len(show_pos)==len(str1)):
	print("You guess right")




