def moveZeroes():
    MyInput = input("Give me a list of elements separated by a space.")
    nums = MyInput.split()
    indexZero = []
    for num in nums:
        if num == "0":
            indexZero.append(num)

    for zero in indexZero:
        nums.remove(zero)

    for i in range(len(indexZero)):
        nums.append(0)

    print(nums)


class Solution:
    moveZeroes()