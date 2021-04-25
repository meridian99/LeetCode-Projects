def detectCapitalUse():
    word = input("Give me any word: ")
    numCaps = 0
    for i in word:
        if i.isupper():
            numCaps += 1

    if len(word) == numCaps:
        print("The use of capitals is correct.")

    if numCaps == 0:
        print("The use of capitals is correct.")

    if word[0].isupper() and numCaps == 1:
        print("The use of capitals is correct.")

    if word[0].islower() and 0 < numCaps < len(word) or word[0].isupper() and 1 < numCaps < len(word):
        print("No, the use of capitals is not correct.")

class Solution:
    detectCapitalUse()