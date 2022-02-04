# import counter
from collections import Counter

# input string to check
def isPalPer(s):
    # Create a counter object for data with key value pair of element and their occurance
    # Initialise odd as 0
    cnt = Counter(s)
    odd = 0
    # iterate through each element in the counter object
    for freq in cnt.values():
        # if freq is odd increase odd count by 1
        if freq%2 != 0:
            odd += 1
            # if odd count is more than one return False
            if odd>1:
                return False
    return True

s = 'geeksforgeeks'
s2 = 'aabbc'
print(isPalPer(s))
print(isPalPer(s2))