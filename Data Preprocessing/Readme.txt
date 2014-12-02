Jigar Chandra (chandra.67@osu.edu)
Gaurav Shah (shah.889@osu.edu)

==========================
Data Mining - Assignment 1
==========================

Executing the program
---------------------
1) Run command "bash run.sh" to execute the python program.
Before actual execution starts, you will see these two lines printed on console:
': not a valid identifier
': not a valid identifier

Please note these are not errors in program.

Files Involved :
-----------------------
/home/5/chandraj/Data Mining/tester.py
/home/5/chandraj/Data Mining/mod1.py


Viewing Output
--------------
After running bash run.sh,
the terminal will output the status of the code execution as follows:
1)For every sgm file it is currently processing, it will output a corresponding print statement:
	CURRENT URL : <the file currently being read and processed>
 
2)Also while creating a dictionary of the unique words(keys) and in how many articles they appear(values). To show the status of the terms checked,
after every 1000 words there will be the count of words that are checked. This dictionary creation is the most-time consuming part of the program and will roughly take 5-7 mins to complete.
	NO OF TERMS CHECKED: <count of the terms checked>
 
After the dictionary is generated, you will be asked to enter the thresholding limits
Enter 99 for maximum thresholding rate
and 1 for minimum thresholding rate
 
The output generated consists of following files:

1) /home/5/chandraj/Data Mining/fv1.txt
BINARY VECTOR:
A Vector for each article, which contains an entry for each of the extracted wordlist as 1 or 0 if the word appears atleast once in that article or not. 

Eg:

DOC ID:1
TOPICS:['cocoa']
PLACES:['el-salvador', 'usa', 'uruguay']
BINARY LIST OF WORDS:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

2)/home/5/chandraj/Data Mining/fv2.txt
TRANSACTION MATRIX: 
Transaction matrix is a list which provides a list of unique words appeared in each article. Whenever it is an empty set, it denotes that all the unique words which were originally present in the article have been removed by thresholding.

Eg:

DOC ID:1
TOPICS:['cocoa']
PLACES:['el-salvador', 'usa', 'uruguay']
LIST OF WORDS:set([‘weekli', ‘held', ‘publish', ‘go', ‘still', ‘rose', ‘late', ‘farmer', ‘earli', ‘good', ‘march', ‘around', ‘buyer', ‘trade', ‘name', ‘level', ‘februari', ‘januari', ‘mean', ‘certif', ‘contin’, ‘crop', ‘export', ‘expect', ‘year',])


3) /home/5/chandraj/Data Mining/fv3.txt
DOCUMENT TERM MATRIX: 
Data matrix is a list of dictionaries, where every dictionary has the key as one of the words from the universal unique west of words across all documents and the value is the number of occurrences in the article. The index of the dictionary in the list of dictionaries is the article number.

Eg:

['japan', 'consider', 'miner', ‘consum', ‘dollar', ‘month', ‘four' …]
[	0, 	2, 		1, 	  0, 	        4, 	    0, 		0 …]
