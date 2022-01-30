def left_rotate(list):
    list.append(list.pop(0))
    return list

def left_rotate2(list):
    list = list[1:] + list[0:1]
    return list

Input_list = list(map(int, input('Enter the list of numbers').split()))
print(left_rotate(Input_list))
print(left_rotate2(Input_list))