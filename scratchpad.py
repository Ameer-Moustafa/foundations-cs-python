# Linear search

list = [0,7,8,1,2,36,8,1,2,19]

def linearSearch(list, value):
    for i in range(len(list)):
        if(list[i] == value):
            return True
    return False

# O(n)

# Binary search

sorted_list = sorted(list)

def binarySearch(list, value): #O(logN) we are taking have the list
    low = list[0]
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if value == list[mid]:
            return mid
        elif value < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(sorted_list)
print(binarySearch(sorted_list, 36))

# Sorting algos

list = [5,1,4,2,8]

def bubbleSort():
    for x in range(len(list)):
        check_swap = False
        for y in range(len(list) - x - 1):
            if list[y] > list[y+1]
            check_swap = True
            temp = list[y]
            list[y] = list[y+1]
            list[y+1] = temp
    if not check_swap:
        print("The list is sorted")
        return list