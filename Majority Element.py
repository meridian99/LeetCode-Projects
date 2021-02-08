def majorityElement():
    MyInput = input("Give a list of elements separated by a space.")
    nums = MyInput.split()
    occurrences = {}
    for item in nums:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1

    halfLength = len(nums) // 2 + 1
    for key in occurrences.keys():
        if occurrences.get(key) >= halfLength:
            print(key)

class Solution:
    majorityElement()