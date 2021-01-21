# returns true if needle is in haystack at index
def matchesAt(haystack: str, needle: str, index: int):
    haystack = input("Give me a string.")
    needle = input("Give me a needle to hide in the haystack.")
    # check to see if needle at index runs off the end of haystack
    if index + len(needle) > len(haystack):
        return False

    # starting at index, does needle match in haystack?
    # loop through needle, check every character
    for needleIndex in range(len(needle)):
        if haystack[index + needleIndex] != needle[needleIndex]:
            # one character did not match, so give up at this index
            return False

    # all characters matched, so found needle here
    return True

def strStr():
    haystack = input("Give me a string.")
    needle = input("Give me a needle to hide in the haystack.")
    if needle == "":
        return 0

    # loop through the haystack and check for needle at every index
    # if found, return the (first) index
    for index in range(len(haystack)):
        if matchesAt(haystack, needle, index):
            return index

    return -1


def strstr():
    haystack = input("Give me a string.")
    needle = input("Give me a needle to hide in the haystack.")
    if len(haystack) == 0:
        if len(needle) == 0:
            return 0
        else:
            return -1

    if needle in haystack:
        return haystack.index(needle)
    return -1

class Solution:
    strstr(haystack, needle)