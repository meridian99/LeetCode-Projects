def fib():
    n = int(input("Give me a number: "))
    if n <= 1:
        return n

    if n == 2:
        return 1

    sum = 0
    i1 = 1
    i2 = 1
    for i in range(3, n + 1):
        sum = i1 + i2
        i2 = i1
        i1 = sum

    print(sum)

class Solution:
    fib()