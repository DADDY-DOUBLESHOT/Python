import ast


common_list=[]


def common_finder(file1,file2):
	file1_open=open(file1+".txt","r")
	file2_open=open(file2+".txt","r")
	file1_content=file1_open.read()
	file2_content=file2_open.read()
	
	# list1=file1_content.split(",")
	# list2=file2_content.split(",")
	list1=(ast.literal_eval('['+file1_content+']'))
	list2=(ast.literal_eval('['+file2_content+']'))
	for i in list1:
		if(i in list2):
			common_list.append(i)
	print("The common Elements were : ",str(common_list)[1:-1])



# -------------------main--------------------

name1,name2=input("Enter the name of two files containing numbers without .txt extension\n"),input()

common_finder(name1,name2)
