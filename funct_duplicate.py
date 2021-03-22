#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.


def funct_duplicate(List):
	return list(set(List))

#main prog

List=[1,2,3,4,5,1,23,3,2]
print(funct_duplicate(List))