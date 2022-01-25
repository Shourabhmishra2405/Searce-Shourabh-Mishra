Maximum = [0]
for i in range(int(input())):
    nums = list(map(int, input().split()))
    if nums[0] == 1:
        Maximum.append(max(nums[1], Maximum[-1]))
    elif nums[0] == 2:
        Maximum.pop()
    else:
        print(Maximum[-1])