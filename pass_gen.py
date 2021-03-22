import random

weaks=[123456,"password",123456789,12345,12345678,"qwerty",1234567,111111,1234567890,123123,"abc123",1234,"password1","iloveyou","1q2w3e4r",000000,"qwerty123","zaq12wsx","dragon","sunshin","princess","letmein",654321,"monkey",27653,"1qaz2wsx",123321,"qwertyuiop","superman","asdfghjkl"]
nums=[1,2,3,4,5,6,7,8,9,0]
chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','w','x','y','z']
syms=['~','`','!',' ','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|','\\',':',';','"',"'",'<',',','>','.','?','/']
def generate(type):
	if(type==1):
		return random.choice(weaks)
	elif(type==2):
		return str(str(random.choice(weaks))+str(random.choice(syms))+str(random.choice(nums)))
	else:
		return str(str(random.choice(chars))+str(random.choice(syms))+str(random.choice(nums))+str(random.choice(nums))+str(random.choice(chars))+str(random.choice(syms))+str(random.choice(syms))+str(random.choice(nums))+str(random.choice(chars)))




usrtype=int(input("How Strong Password \n 1: weak \n 2: medium \n 3: hard\n"))
print(generate(usrtype))