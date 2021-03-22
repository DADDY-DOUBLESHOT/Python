import ast
import json
file1=open("input.txt","r+")
file2=open("output.txt","w+")




file1_content=file1.read().split("\n");
itr=iter(file1_content)
dump=dict(zip(itr,itr))
json.dump(dump,file2)
file2.close()
file1.close()
birthday=open("output.json","r")
birth=json.load(birthday)
for key in birth:
	print(key)
