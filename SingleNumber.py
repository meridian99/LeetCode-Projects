def singleNumber():
    nums = list(input("Make a list with every element appearing once except one, ex: [4,4,5,6,7,6,7]"))
    # Puts every number into my list once
    my_list = []
    for number in nums:
        if number not in my_list:
            my_list.append(number)

    # Then removes it from nums here so it doesn't mess it up while adding.
    for number in my_list:
        nums.remove(number)

    # Goes through the numbers in nums and removes all the ones that match inside my_list.
    for single in nums:
        if single in my_list:
            my_list.remove(single)

    # Returns the first element in my_list which should be the one that appears only once.
    return my_list[0]

class Solution:
    singleNumber()