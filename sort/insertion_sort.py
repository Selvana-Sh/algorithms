# takes the element at index zero. That element would be "sorted". repeadely compares elements of "unsorted" list
# to the sorted ones and adds them to "sorted".
# Complexity: average and worst-case O(n^2)

def insertion_sort(arr):
    for i in range(1, len(arr)): # not the first one, already in sorted
        temp = arr[i] # the one you compare 
        j = i - 1 # element previous to temp

        while j >= 0 and arr[j] > temp:
            arr[j+1], arr[j] = arr[j], arr[j+1] # swap temp's position with the element at a[j]
            j -= 1 # for comparing the rest of the "sorted" part
        arr[j+1] = temp # if the temp wasn't bigger, move forward

    return arr