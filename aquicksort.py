#quicksort implementation in python with array
def quicksort_array(arr):

#1. choosing a pivot element
#2. partitioning the array into elements less than equal to and greater than the pivot
#3. recursively sorting the partitions
    
#time complexity: O(n log n) average O(n²) worst case
#space complexity: O(log n) average for recursion stack

    # base case: if array has 0 or 1 element it's already sorted
    if len(arr) <= 1:
        return arr

    # choose pivot (middle element)
    pivot = arr[len(arr) // 2]
    
    # partition: divide array into three parts
    left = [x for x in arr if x < pivot]   # elements smaller than pivot
    mid  = [x for x in arr if x == pivot]  # elements equal to pivot
    right = [x for x in arr if x > pivot]  # elements greater than pivot

    # recursively sort left and right partitions, then combine
    return quicksort_array(left) + mid + quicksort_array(right)
