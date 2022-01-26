# Defining the function to reverse the elements present in the list P with the starting index start and ending index end.
def reverseList(P, start, end):
    while start < end:
        P[start], P[end] = P[end], P[start]
        start += 1
        end -= 1
    for x in range(len(P)):
        print(P[x],end = ' ')
# Taking inputs from user
# Input for number of integer to reverse.
n = int(input('Enter Number of integers'))
# Input for numbers to reverse.
arr = list(map(int, input().split()))
reverseList(arr,0,n-1)
