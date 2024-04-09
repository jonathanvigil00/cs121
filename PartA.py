import sys
import os

#have a current token working on and keep adding to it until break.
# This fixes readline breaking up that character by keeping it in memory after the next readline
def tokenize(filePath):
    tokens = {}
    current_word = ""
    with open(filePath, 'r') as file:
        line = file.readline(100)
        while line:
            print(line)
            line = file.readline(100)

def computeWordFrequency(tokenList):
    pass

def printFrequencies(wordCount):
    pass

def checkArgs():
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print("File path filePath does not exist. Exiting...".format(filepath))
        sys.exit()


if __name__ == "__main__":
    checkArgs()
    tokenize(sys.argv[1])
    # perform argument check
    # read in file
    # tokenize in file
    # computer word frequencies
    # print frequencies
    # handle additional errors

    # to run: python3 partA.py test.txt