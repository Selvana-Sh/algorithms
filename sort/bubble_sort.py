# swap if the element found is greater than the next element
# complexity: average and worst-case: O(n^2)

def bubble(seq):
    n = len(seq)-1 # to not swap the last element
    swapped = True  # enter the loop
    
    while swapped:
        swapped = False  # reset for every iteration
        
        for i in range(1, n):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                swapped = True # continue the loop 
    return seq
