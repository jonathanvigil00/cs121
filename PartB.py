import PartA as A
import sys
import os

"""
Run-time Analysis: O(n+m), n being tokens in file 1 and m tokens in file 2

Explanation: Both lists are converted to sets to remove duplicates (lower amount fo elements
to iterate over) and make lookups efficient. This process takes O(n+m) time.
The function determines the smaller list and uses that one to iterate over,
and this takes min(n, m) time. Once the smaller set is found, it iterates over each element in O(min(n, m)) time 
and checks if it is present in the other set. Because it is a set which is hashable, lookup is O(1).
The run-time complexity is creating the sets at O(n+m) time.
"""
def countCommonTokens(file1_tokens, file2_tokens):
    list1 = set(file1_tokens)
    list2 = set(file2_tokens)

    if len(list1) > len(list2):
        list1, list2 = list2, list1

    common_token_count = 0
    for token in list1:
        if token in list2:
            common_token_count += 1
    print(common_token_count)
    return common_token_count

if __name__ == "__main__":
    # perform argument checks
    if len(sys.argv) > 2 and A.checkArgs(sys.argv[1]) and A.checkArgs(sys.argv[2]):

        # read in files and tokenize files
        tokens1, tokens2 = A.tokenize(sys.argv[1]), A.tokenize(sys.argv[2])

        # count common tokens and print them
        countCommonTokens(tokens1, tokens2)

        # handle any additional errors