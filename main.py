def trailingzeroes():
    n = int(input("Give me a number with trailing zeros or none."))
    # Calculate the factorial value n!
    counter = 1
    for number in range(1, n + 1):
        counter *= number

    # Convert to string
    reverse = str(counter)[::-1]

    # Count the zeros
    numberofzeros = 0
    for numeral in reverse:
        if numeral == "0":
            numberofzeros += 1
        else:
            break

    print("There are, " + str(numberofzeros) + " behind this number.")

class Solution:
    trailingzeroes()