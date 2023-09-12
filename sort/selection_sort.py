# set min to the first item in the list, swap until you find a new min
# Complexity: average and worst-case: O(n^2)

def selection_sort(seq):

    for i in range(0, len(seq) - 1):
        min = i # assume first item is min

        for j in range(i+1, len(seq)): # check after the min (unsorted part)
            if seq[j] < seq[min]:
                min = j
        
        if min != i: # new min exists, need to swap
            seq[min] , seq[i] = seq[i], seq[min]

    return seq