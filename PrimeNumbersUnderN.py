def countPrimes():
    n = int(input("Give me a number."))
    if n < 9:
        if n <= 2:
            return 0
        if n == 3:
            return 1
        if n == 4:
            return 2
        if n == 5:
            return 2
        if n == 6:
            return 3
        if n == 7:
            return 3
        if n == 8:
            return 4

    primeCounter = [2, 3, 5, 7]
    numPrimes = 4
    for number in range(11, n):
        isPrime = True
        for prime in primeCounter:
            # tried divmod to make it one operation, but it's slower for small numbers
            # if (prime > 1000000):
            #    a,b = divmod(number, prime)
            #    if prime > a:
            #        break
            #    if b == 0:
            #        isPrime = False
            #        break
            # else:
            if prime > number / prime:
                break
            if number % prime == 0:
                isPrime = False
                break
        if isPrime:
            primeCounter.append(number)
            numPrimes += 1

    return numPrimes


class Solution:
    countPrimes()