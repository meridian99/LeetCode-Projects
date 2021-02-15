def addDigits():
    num = int(input("Give me a number"))
    numsum = 0
    while True:
        if len(str(num)) == 1:
            break

        for number in str(num):
            numsum += int(number)

        num = numsum
        numsum = 0

    print(num)

class Solution:
    addDigits()