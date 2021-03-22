
def turnIntoList(List):
	return list(set(List))


listA=[1,1,2,2,3,4,5,5]
listB=turnIntoList(listA)
print(listB)