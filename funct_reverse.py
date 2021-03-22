#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order

def funct_reverse(string):
	list=string.split(" ")
	return " ".join(list[::-1])


string =input("Enter some words to reverse")
print(funct_reverse(string))