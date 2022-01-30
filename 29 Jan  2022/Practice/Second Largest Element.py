def getsecmax(list):
    if len(list) <=1:
        return None
    lar = list[0]
    slar = None
    for x in list[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif x < lar:
            if slar == None or slar<x:
                slar = x
    return print(slar)

Input_list = list(map(int,input('Enter the list of numbers').split()))
getsecmax(Input_list)