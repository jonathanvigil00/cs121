Assignment 1
Jonathan Bryant Vigil
jbvigil@uci.edu


To run Part A: python3 PartA.py <filename>
To run Part B: python3 PartB.py <filename1> <filename2>


How it works:

Part A main function - Takes in a filename as a parameter in the command line and does error checks.
Calls the tokenizer function which opens the file and parses the text, returning a list of tokens of
alphanumeric characters. A dictionary is then used to map each token to how many times
they appear in the list. This map is then iterated through and added to a new list which sorts 
lexicographically and then by frequency count to ensure count is the first priority of sorting. 
This sorted list is then printed out in sorted order.

Part B main function - Takes in 2 filenames in the command line and does error checks on them.
Uses tokenize function from part A to return a list of tokens for each file.
countCommonTokens is called with both lists as parameters. 
Makes both lists into sets to avoid duplicates and itereates over the smaller list, checking
if the token is present in the other. Returns the number of common tokens.


Purpose:
The reason for creating the tokenizer with token counts in part A is to count how many 
occurances of a token is present in a file. Then in part B, it counts how many tokens
are present in both files. The more tokens in common that they share, the more similar 
both files are. This can be a way to rank how similar two sequence of words are and 
can be used to rank them, which has many applications such as in a search engine.

Sources used:
https://stackabuse.com/read-a-file-line-by-line-in-python/