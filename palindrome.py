str1=input("Enter a string : ")
str2=str1[::-1]
# if(str1==str2):
# 	print("PALINDROME")
# else:
# 	print("NOT PALINDROME")
flag=0
itr=int(0)
for i in str1:
	if(str1[itr]!=str2[itr]):
		print("NOT PALINDROME")
		break
	else:
		flag+=1

if(flag!=0):
	print("PALINDROME")