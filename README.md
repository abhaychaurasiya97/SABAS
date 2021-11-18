# SABAS
Play with text and applaud us by saying "SABAS".
Its search method is based on KMP (Knuth-Morris-Pratt) Algorithm.
Its operations are Search ,Delete(All), Replace(All), Delete and Replace Multiple word of same occurence of pattern according to index
# Time Complexity:
  O(m+n)
  n-length of pattern
  m-length of text





# open console and type
	sabas -h or --help
	 command -option [filename] [pattern] [new_string]
		new_string is only for replacement leave it blank if not needed.
	
	Option 		 Description
#
	-->	default		Search all the occurence of pattern in text file
#
	`-->	-r		replaces all the occurence of pattern in text file with new_string
#
	 or --replace
#
 	new_string is for only replacement for any other operation leave it blank 
#
	-->	-rm		replaces multiple occurence of pattern with specified index in text file with new_string

	 or --replace-multiple
#
	-->	-d		delete all the occurence of pattern in text file
	 or --delete
#
	-->	-dm		delete multiple occurence of pattern with specified index in text file 
	 or --delete-multiple

                                                                                                         
