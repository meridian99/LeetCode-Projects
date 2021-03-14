def findTheDifference():
    s = input("Give me a string: ")
    t = input("Give me another string with only one difference from the other string: ")
    letters = {}
    for i in t:
        if i in letters:
            letters[i] += 1

        else:
            letters[i] = 1

    for key in letters.keys():
        if key not in s:
            print(key + " is the difference between the strings")

        else:
            if letters.get(key) > s.count(key):
                print(key + " is the difference between the strings")

    if s == t:
        print("Sir, there is no difference.")

class Solution:
    findTheDifference()