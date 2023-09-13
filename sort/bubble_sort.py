# swap if the element found is greater than the next element
# sort in ascending order 
# complexity: average and worst-case: O(n^2)

def bubble(arr):
    n = len(arr)-1 # to not swap the last element
    swapped = True  # enter the loop
    
    while swapped:
        swapped = False  # reset for every iteration
        
        for i in range(1, n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True # continue the loop 
    return arr
