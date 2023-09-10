from random import randint
from time import time

def simple_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return i
    return -1

def binary_search(my_list, target, low=None, high=None):  # list must be sorted
    if low is None:
        low = 0
    if high is None:
        high = len(my_list) - 1
    
    if high < low: # target not found
        return -1
    
    mid = (low + high) // 2

    if my_list[mid] == target:
        return mid
    elif target < my_list[mid]:
        return binary_search(my_list, target, low, mid-1)
    else:
        return binary_search(my_list, target, mid+1, high)
    
if __name__ == "__main__":
    # initializing the list
    length = 1000
    sorted_list = set()
    
    while len(sorted_list) < length:
        sorted_list.add(randint(-2*length, 2*length))
    sorted_list = sorted(list(sorted_list))

    # time
    start = time()
    for target in sorted_list:
        simple_search(sorted_list, target)
    end = time()
    print("Simple search: ", (end - start)/length, " seconds")

    start = time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time()
    print("Binary search: ", (end - start)/length, " seconds")
