def containsDuplicate():
    nums = list(input("Give me a list with only numbers that appear once except one number."))
    numbers = {}
    for num in nums:
        if num not in numbers:
            numbers[num] = 1

        else:
            numbers[num] += 1
    counter = len(numbers)
    for value in numbers.values():
        if value > 1:
            print("True, this list has a duplicate number.")


class Solution:
    containsDuplicate()