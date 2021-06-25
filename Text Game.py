import random
def randomString():
    randomString = ""
    count = 0
    fifty = ["1", "2"]
    test_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    while True:
        randomchoice = (random.choice(test_list))

        if randomchoice.isalpha():
            fiftychance = random.choice(fifty)
            if fiftychance == "1":
                randomString += randomchoice.upper()
            else:
                randomString += randomchoice.lower()
        else:
            randomString += randomchoice

        count += 1
        if count == 32:
            print(randomString)
            return False

class Solution:
    randomString()
