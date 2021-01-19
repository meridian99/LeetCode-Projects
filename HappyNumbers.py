def isHappy():
    n = int(input("Give me a number"))
    oldSums = {}
    currentSum = 0
    oldSum = n
    while True:
        for num in str(oldSum):
            val = int(num)
            power = val * val
            currentSum += power

        if currentSum == 1:
            print("This number is a happy number.")
            break
        if currentSum in oldSums:
            print("This number is not a happy number.")
            break
        oldSums[currentSum] = 1
        oldSum = currentSum
        currentSum = 0


class Solution:
    isHappy()