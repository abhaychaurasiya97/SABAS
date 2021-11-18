# SABAS
Play with text and applaud us by saying "SABAS".

Its search method is based on KMP (Knuth-Morris-Pratt) Algorithm.
# Time Complexity:
  O(m+n)
  n-length of pattern
  m-length of text






#	sabas -h or --help
# command -option [filename] [pattern] [new_string]

	Option 		 Description

-->	default		Search all the occurence of pattern in text file
#
-->	-r		replaces all the occurence of pattern in text file with new_string
#
	 or --replace
#
 	new_string is for only replacement for any other operation leave it blank 
#
-->	-rm		replaces multiple occurence of pattern with specified index in text file with new_string

	 or --replace-multiple

-->	-d		delete all the occurence of pattern in text file
	 or --delete

-->	-dm		delete multiple occurence of pattern with specified index in text file 
	 or --delete-multiple

                                                                                                         
