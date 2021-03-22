



def writer(file_name,para):
	file_new_name=file_name+".txt"
	file_open=open(file_new_name,"w+")
	file_open.write(str(para))
	file_open.close()

def reader(file_name):
	file_new_name=file_name+".txt"
	file_open=open(file_new_name,"r+")
	para=file_open.read()
	print(para)
	file_open.close()




name=input("Enter a name for the file ")
whole_string=input("Enter a string to write to the file")
writer(name,whole_string)
print("Do you want to read from the file ",name,".txt,\n 1: Yes  \n 2: No\n")
ans=int(input())
if(ans==1):
	reader(name)