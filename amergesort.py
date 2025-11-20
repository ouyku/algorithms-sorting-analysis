#merge sort implementation in python with array
def mergesort_array(arr):

#1. dividing the array into two halves
#2. recursively sorting each half
#3. merging the two sorted halves back together
    
#time complexity: O(n log n) always
#space complexity: O(n) for temporary arrays

    # base case: if array has 0 or 1 element it's already sorted
    if len(arr) <= 1:
        return arr

    # divide: split the array into two halves
    mid = len(arr) // 2
    left = mergesort_array(arr[:mid])   # sort left half
    right = mergesort_array(arr[mid:])  # sort right half

    # conquer: merge the two sorted halves
    return merge(left, right)

def merge(left, right):
    
#merges two sorted arrays into one sorted array
#this function compares elements from both arrays and combines them in sorted order

    merged = []
    i = j = 0  # pointers for left and right arrays

    # compare elements from both arrays and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # add any remaining elements from left array
    merged.extend(left[i:])
    # add any remaining elements from right array
    merged.extend(right[j:])
    return merged
