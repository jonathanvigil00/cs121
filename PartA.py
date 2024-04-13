import sys
import os

"""
Run-time Analysis: O(n), n being the num of char in the file

Explanation: All the characters must be processed in the file which is O(n) time.
The processing steps in the loop are constant so the method simplifies
 to O(n) total time.
"""
def tokenize(filePath):
    tokens = []
    current_word = ""

    with open(filePath, 'r') as file:
        line = file.readline(100)
        while line:
            for char in line:
                ord_char = ord(char)
                if (ord_char >= 97 and ord_char <= 122) or (ord_char >= 48 and ord_char <= 57):
                    current_word += char
                elif ord_char >= 65 and ord_char <= 90:
                    current_word += char.lower()
                else:
                    if current_word != "":
                        tokens.append(current_word)
                    current_word = ""

            line = file.readline(100)

        if current_word:
            tokens.append(current_word)
    return tokens

"""
Run-time Analysis: O(n), n being number of tokens

Explanation: Each token is processed and added/incremented into the new dictionary.
This process is O(n) time.
"""
def computeWordFrequency(tokenList):
    token_map = {}
    for token in tokenList:
        if token in token_map:
            token_map[token] += 1
        else:
            token_map[token] = 1
    return token_map

"""
Run-time Analysis: O(nlogn), n being size of parameter dictionary

Explanation: The dictionary is converted to a list which is O(n) time.
The list is then sorted twice which simplifies to O(nlogn) since it is 
the most expensive computation.
"""
def printFrequencies(wordCount):
    sorted_list = [(key, count) for key, count in wordCount.items()]
    sorted_list.sort(key=lambda x: x[0])
    sorted_list.sort(key=lambda x: x[1], reverse=True)
    
    for token in sorted_list:
        print(f'{token[0]} = {token[1]}')

"""
Run-time Analysis: O(1), constant

Explanation: The function does a lookup of the file path in 
a hashtable or other similar structure which is constant.
"""
def checkArgs(filepath):
    if not os.path.isfile(filepath):
        print(f"File path {filepath} does not exist. Exiting...")
        return False
    return True


if __name__ == "__main__":
    # perform argument check
    if len(sys.argv) > 1 and checkArgs(sys.argv[1]):

        # read in file and tokenize in file
        tokens = tokenize(sys.argv[1])

        # compute word frequencies
        token_count = computeWordFrequency(tokens)

        # print frequencies
        printFrequencies(token_count)