def left_rotate_d_places(list,n):
    for i in range(n):
        list.append(list.pop(0))
    return list

Input_list = list(map(int, input('Enter the list of numbers').split()))
n = int(input('Enter No. of places to be shifted'))
print(left_rotate_d_places(Input_list,n))