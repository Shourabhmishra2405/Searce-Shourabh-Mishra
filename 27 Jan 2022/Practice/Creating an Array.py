from array import *
arr = array('i',[1,2,3,4,5])
arr2 = array('i',[1,2,3,4,5])

# print(arr2)

# arr2.insert(5,6)
# print(arr2)

def traverseArray(array):
    for i in array:
        print(i)

# traverseArray(arr2)

def accessElement(array, index):
    if index > len(array):
        print('There is not any element in this index')
    else:
        print(array[index])

# accessElement(arr,2)
# arr[2]

def searchInArray(array,value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element does not exist in this array"

# print(searchInArray(arr,5))

arr.remove(3)

print(arr)
