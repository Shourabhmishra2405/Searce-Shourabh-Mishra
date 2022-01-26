# Initialising and empty list
Maximum = []
# Iterating for n number of times according to user input
for i in range(int(input())):
    # Seperating out the inputs into operation and value to input
    nums = list(map(int, input().split()))
    # Operations according to the inputs
    if nums[0] == 1:
        Maximum.append(max(nums[1], Maximum[-1]))
    elif nums[0] == 2:
        Maximum.pop()
    else:
        print(Maximum[-1])
