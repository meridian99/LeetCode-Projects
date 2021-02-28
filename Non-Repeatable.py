def firstUniqChar():
    s = input("Give me a string: ")
    occurrences = {}
    for letter in s:
        if letter in occurrences:
            occurrences[letter] += 1

        else:
            occurrences[letter] = 1

    for key in occurrences.keys():
        if occurrences.get(key) == 1:
            print(key + " is the first unique letter")
            break
    if all(value >= 2 for value in occurrences.values()):
        print("There is no unique letter")

class Solution:
    firstUniqChar()