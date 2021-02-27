def canConstruct():
    replica = ""
    note = input("Give me a string: ")
    magazine = input("Give me another string: ")
    letters = {}
    for letter in magazine:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    for letter in note:
        if letter in letters.keys():
            replica += letter
            if letter == 0:
                print("No, the first string can not be constructed from the second string.")
                break
            letters[letter] -= 1

        else:
            print("No, the first string can not be constructed from the second string.")
            break
    if replica == note:
        print("Yes, the first string can be constructed from the second string.")

class Solution:
    canConstruct()