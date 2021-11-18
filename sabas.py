import sys
import os
count=[]
lsp=[0]
def lsp_array(pattern):#for finding longest suffix and prefix
	l=0 #l stands for length of same prefix and suffix match  
	i=1
	global lsp
	while i<len(pattern):
		if pattern[l]==pattern[i]:
			lsp.append(l+1)
			l+=1
			i+=1
		else:
			if l!=0:
				l=lsp[l-1]
				
			else:
				lsp.append(0)
				i+=1
	return lsp
			
def search (text,pattern):
	global count
	global lsp
	lsp=lsp_array(pattern)
	i=0
	j=0
	while i<len(text):
		if text[i]==pattern[j]:
			i+=1
			j+=1
		else:
			if j!=0:
				j=lsp[j-1]	
			else:
				i+=1
		if j==len(pattern):
			
			count.append(i-j)
			
			j=lsp[j-1]
	print("->",end='')
	print(f" {len(count)} match found at index {count}")
def delete(text,pattern):
	new_text=''
	search(text,pattern)
	if len(count)==0:
		print("No match found")
	else:
		text=text.replace(pattern,'')
		create_file(text)
		print("Do you want to see the text y/n")
		if input()=='y':
			print(text)
		else:
			print("Deleted")
def replace(text,pattern,new_string):
	
	search(text,pattern)
	if len(count)==0:
		print("No match found")
	else:
		i=0
		text=text.replace(pattern,new_string)
		create_file(text)
		print("Do you want to see the text y/n")
		if input()=='y':
			print(text)
		else:
			print("Replaced")
			
	
	
			

def help():
	print("\tsabas -h or --help")
	print("\tCommand -option [filename] [pattern] [new_string]\n")
	print("\tOption \t\t Description\n")
	print("-->\tdefault\t\tSearch all the occurence of pattern in text file\n")

	print("-->\t-r\t\treplaces all the occurence of pattern in text file with new_string")
	print("\t or --replace")
	print("\tnew_string is for only replacement for any other operation leave it blank ")
	print("-->\t-rm\t\treplaces multiple occurence of pattern with specified index in text file with new_string\n")
	print("\t or --replace-multiple\n")
	print("-->\t-d\t\tdelete all the occurence of pattern in text file")
	print("\t or --delete\n")
	print("-->\t-dm\t\tdelete multiple occurence of pattern with specified index in text file ")
	print("\t or --delete-multiple\n")
def check_for_index(index):
	global count
	for i in index:
		if i not in count:
			print("Enter Correct Index")
			return False
	return True 
def replace_multiple(text,pattern,new_string):
	
	global count
	search(text,pattern)
	index=[int(x) for x in input("Enter Multiple integer input with space separated").split()]
	index.sort()
	if len(count)==0:
		print("No match found")
	
	elif check_for_index(index):
		new_text=''
		i=0
		for j in index:
			new_text+=text[i:j]+new_string
			i=j+len(pattern)
		if len(text[j:])!=len(pattern):
			new_text+=text[j:len(text)]
				
		create_file(new_text)	
		print("Do you want to see the text y/n")
		if input()=='y':
			print(new_text)
		else:
			print("Replaced")
def delete_multiple(text,pattern):
	global count
	search(text,pattern)
	index=[int(x) for x in input("Enter Multiple integer input index with space separated").split()]
	index.sort()
	if len(count)==0:
		print("No match found")
	
	elif check_for_index(index):
		new_text=''
		i=0
		for j in index:
			new_text+=text[i:j]+''
			i=j+len(pattern)
		if len(text[j:])!=len(pattern):
			new_text+=text[j:len(text)]
				
		create_file(new_text)	
		print("Do you want to see the text y/n")
		if input()=='y':
			print(new_text)
		else:
			print("Deleted")
	
def check_option():
	
	if sys.argv[1] in ['-h','-d','-r','-dm','-rm','--replace','--delete-multiple','--replace-multiple','--help']:
		return True
	elif sys.argv[1][0]!='-':
		try:
			search(open_file(sys.argv[1]),sys.argv[2])
			return False
		except:
			help()
	elif sys.argv[1] not in ['-h','-d','-r','-dm','-rm','--replace','--delete-multiple','--replace-multiple','--help'] and sys.argv[1][0]=='-':
		help()
		return False
def create_file(text):
	
	
	with open(check_existence_of_file(),'x') as f:
		f.write(text)
		f.close()
def open_file(filename):
	if filename not in os.listdir():
		print("Enter correct ordered argument or File does not exist !!!")
	else:
		with open(filename) as f:
			return f.read()
	
def check_existence_of_file():
	
	filename='sabas-text'
	
	while True:
		
		if filename not in os.listdir():
			return filename
		filename+='_new'
		
	


try:
	if check_option():
		if sys.argv[1]=='-d' or sys.argv[1]=='--delete':
			delete(open_file(sys.argv[2]),sys.argv[3])
		if sys.argv[1]=='-r'or sys.argv[1]=='--replace':
			replace(open_file(sys.argv[2]),sys.argv[3],sys.argv[4])
		if sys.argv[1]=='-h' or sys.argv[1]=='--help':
			help()
		if sys.argv[1]=='-rm' or sys.argv[1]=='--replace_multiple':
			replace_multiple(open_file(sys.argv[2]),sys.argv[3],sys.argv[4])
		if sys.argv[1]=='-dm' or sys.argv[1]=='--delete_multiple':
			delete_multiple(open_file(sys.argv[2]),sys.argv[3])
except:
	help()

