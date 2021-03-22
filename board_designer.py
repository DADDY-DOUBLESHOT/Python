def create(rows,cols):
	sum=rows*cols
	for i in range(rows):
		print(" ---"*cols)
		print("|   "*(cols+1))
		print(" ---"*cols)
row,col=int(input("Enter the row x cols for matrix\n")),int(input())
create(row,col)