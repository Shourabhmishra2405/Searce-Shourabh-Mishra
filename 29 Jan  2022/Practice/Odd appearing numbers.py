def odd_appearing(list):
    list_of_odd_appearing_numbers = set()
    for x in list:
        count = list.count(x)
        if count%2 !=0:
            list_of_odd_appearing_numbers.add(x)
    return list_of_odd_appearing_numbers

Input_list = list(map(int, input('Enter the list of numbers').split()))
print(odd_appearing(Input_list))