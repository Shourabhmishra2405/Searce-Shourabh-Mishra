def reverseList(P, start, end):
    while start < end:
        P[start], P[end] = P[end], P[start]
        start += 1
        end -= 1
    for x in range(len(P)):
        print(P[x],end = ' ')
n = int(input('Enter Number of integers'))
arr = list(map(int, input().split()))
reverseList(arr,0,n-1)
