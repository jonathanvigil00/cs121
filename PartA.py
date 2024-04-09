import sys
import os

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

def computeWordFrequency(tokenList):
    token_map = {}
    for token in tokenList:
        if token in token_map:
            token_map[token] += 1
        else:
            token_map[token] = 1
    return token_map

def printFrequencies(wordCount):
    sorted_list = [(key, count) for key, count in wordCount.items()]
    sorted_list.sort(key=lambda x: x[0])
    sorted_list.sort(key=lambda x: x[1], reverse=True)
    
    for token in sorted_list:
        print(f'{token[0]} = {token[1]}')


def checkArgs(filepath):
    if not os.path.isfile(filepath):
        print(f"File path {filepath} does not exist. Exiting...")
        return False
    return True


if __name__ == "__main__":
    # perform argument check
    if checkArgs(sys.argv[1]):

        # read in file and tokenize in file
        tokens = tokenize(sys.argv[1])

        # compute word frequencies
        token_count = computeWordFrequency(tokens)

        # print frequencies
        printFrequencies(token_count)

        # handle additional errors

    # to run: python3 partA.py test.txt