def if_sorted(list):
    i = 1
    while i <len(list):
        if list[i] < list[i-1]:
            return print('The list is not sorted')
        i =i+1
    return print('The list is sorted')

Input_list = list(map(int, input('Enter the list of numbers').split()))
if_sorted(Input_list)

