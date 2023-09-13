# takes an unsorted sequence and sorts it out in ascending or descending order
# pivot : just a number we base our comparisons off of

# complexity : average-case O(n log n), worst-case O(n^2) 

def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr[length//2]

    lower = []
    higher = []
    the_pivot = []

    for item in arr:
        if item < pivot:
           lower.append(item)
        elif item > pivot:
           higher.append(item)
        else:
           the_pivot.append(item)

    return quick_sort(lower) + the_pivot + quick_sort(higher)
