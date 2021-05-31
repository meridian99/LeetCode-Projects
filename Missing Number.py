def missingNumber():
    nums = list(input("Give me a list of consecutive numbers starting with 0 with one missing: "))
    nums.sort()
    if nums[len(nums) - 1] != len(nums):
        return len(nums)

    if nums[0] != 0:
        return 0


    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            return nums[i - 1] + 1

class Solution:
    missingNumber()