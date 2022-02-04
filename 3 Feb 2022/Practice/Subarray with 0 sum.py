# Input: list to check
# initialize pre_sum as 0
def isZeroSum(l):
    pre_sum = 0
    h = set()
    # Iterate through the list
    for i in range(len(l)):
        # calculate pre_sum for each index
        pre_sum += l[i]
        # if pre_sum is zero or we have a pre_sum already present in set
        # if pre_sum is present then index for which pre_sum is present have a sum zero
        if pre_sum == 0 or pre_sum in h:
            return True
        # adding each pre_sum for each index
        h.add(pre_sum)
    return False

list = [10,20,30,40,-40]
print(isZeroSum(list))