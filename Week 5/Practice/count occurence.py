def firstIndex(list,value):
    low = 0
    high = len(list)-1
    while low <= high :
        mid = (low+high)//2
        if list[mid] > value:
            high = mid -1
        elif list[mid] <value:
            low = mid+1
        else:
            if mid == 0 or list[mid-1] != list[mid]:
                return mid
            else:
                high = mid-1
    return -1

def lastIndex(list,value):
    low = 0
    high = len(list)-1
    while low <= high :
        mid = (low+high)//2
        if list[mid] > value:
            high = mid -1
        elif list[mid] <value:
            low = mid+1
        else:
            if mid == len(list)-1 or list[mid+1] != list[mid]:
                return mid
            else:
                low = mid+1
    return -1  

def countocc(list,value):
    first = firstIndex(list,value)
    if first == -1:
        return 0
    else:
        return lastIndex(list,value) - first +1


list = [5,10,10,10,10,20,20]
print(countocc(list,10))