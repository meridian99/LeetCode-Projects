def majorityElement():
    nums = list(input("Give a list with a majority element."))
    occurrences = {}
    for item in nums:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1

    halfLength = len(nums) // 2 + 1
    for key in occurrences.keys():
        if occurrences.get(key) >= halfLength:
            return key

class Solution:
    majorityElement()