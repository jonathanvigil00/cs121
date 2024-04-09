import PartA as A
import sys
import os

def countCommonTokens(file1_tokens, file2_tokens):
    list1 = set(file1_tokens)
    list2 = set(file2_tokens)

    if len(list1) > len(list2):
        list1, list2 = list2, list1

    common_token_count = 0
    for token in list1:
        if token in list2:
            common_token_count += 1
            print(token)
    print(common_token_count)
    return common_token_count

if __name__ == "__main__":
    # perform argument checks
    if A.checkArgs(sys.argv[1]) and A.checkArgs(sys.argv[2]):

        # read in files and tokenize files
        tokens1, tokens2 = A.tokenize(sys.argv[1]), A.tokenize(sys.argv[2])

        # count common tokens and print them
        countCommonTokens(tokens1, tokens2)

        # handle any additional errors