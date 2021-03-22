

def reverse(str):
	rev_str=str.split(" ")
	rev_str.reverse()
	rev_str=" ".join(rev_str)
	return rev_str

usrStr=input("Enter a String : ")
print(reverse(usrStr))