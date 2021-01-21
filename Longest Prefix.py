def longestCommonPrefix():
    strs = list(input("Give a list of words with common prefixes. ex: [flower, flow, fly]"))
    if len(strs) == 0:
        print("There is no prefix.")

    firstWord = strs[0]
    longestPrefix = ""
    index = 0
    while index >= 0:
        if len(firstWord) <= index:
            break
        letter = firstWord[index]
        for word in strs:
            if len(word) <= index:
                index = -1
                break
            if word[index] != letter:
                index = -1
                break

        if index >= 0:
            index += 1
            longestPrefix += letter

    print(longestPrefix + " is the longest prefix.")

class Solution:
        longestCommonPrefix()