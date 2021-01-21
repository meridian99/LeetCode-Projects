def twoSum():
    target = int(input("Give a number."))
    nums = list(input("Give a list so two numbers can add together to reach the target. Do not have multiple solutions"))
    # Important note: this scrambles the indexes!
    sortedNums = nums.copy()
    sortedNums.sort()
    leftIndex = 0
    rightIndex = len(nums) - 1

    # We home in on the two indexes by seeing if the two indexes we added are equal to our target and if not we move an index over.
    while True:
        total = sortedNums[leftIndex] + sortedNums[rightIndex]
        if total == target:
            break
        if total > target:
            rightIndex -= 1
        else:
            leftIndex += 1

    # since indexes are scrambled, retrieve the VALUES
    addend1 = sortedNums[leftIndex]
    addend2 = sortedNums[rightIndex]

    # find index of values in INPUT array
    finalIndex1 = nums.index(addend1)
    finalIndex2 = nums.index(addend2)

    # we may have duplicate VALUES, but index() returns index of first one
    # so, slice off from first to find the index of second occurrence
    if finalIndex1 == finalIndex2:
        finalIndex2 = nums[finalIndex1 + 1:len(nums)].index(addend2) + finalIndex1 + 1

    return [finalIndex1, finalIndex2, "These are the two indexes."]

class Solution:
    twoSum()


