#quicksort implementation in python with linked list
class Node:

#a simple node class for linked lists
#each node stores a value and a reference to the next node

    def __init__(self, val):
        self.val = val
        self.next = None


def quicksort_linked_list(head):

#sorts a linked list using the Quick Sort algorithm
    
#quick Sort works by:
# 1. choosing a pivot element
# 2. partitioning the list into elements less than equal to and greater than the pivot
# 3. recursively sorting the partitions

#time complexity: O(n log n) average and O(n²) worst case
#space complexity: O(log n) average for recursion stack

    # base case: if list is empty or has one element it's already sorted
    if not head or not head.next:
        return head

    # partition the list around the pivot
    less, equal, greater = partition(head)

    # recursively sort the less and greater partitions
    less = quicksort_linked_list(less)
    greater = quicksort_linked_list(greater)

    # concatenate: less + equal + greater
    result = concatenate(less, equal)
    result = concatenate(result, greater)
    return result


def partition(head):

#partitions a linked list into three parts based on a pivot value
#returns three lists
#less: elements smaller than pivot
#equal: elements equal to pivot
#greater: elements greater than pivot

    if not head or not head.next:
        return head, None, None

    # choose first element as pivot
    pivot = head.val
    
    # create three lists to hold partitioned elements
    less_head = less_tail = None
    equal_head = equal_tail = None
    greater_head = greater_tail = None

    # traverse the list and partition elements
    current = head
    while current:
        if current.val < pivot:
            less_head, less_tail = append_node(less_head, less_tail, current.val)
        elif current.val == pivot:
            equal_head, equal_tail = append_node(equal_head, equal_tail, current.val)
        else:
            greater_head, greater_tail = append_node(greater_head, greater_tail, current.val)
        current = current.next

    return less_head, equal_head, greater_head

def append_node(head, tail, val):

#appends a new node with the given value to the end of a linked list
#returns the updated head and tail of the list

    node = Node(val)
    if not head:
        return node, node
    tail.next = node
    return head, node


def concatenate(a, b):

#concatenates two linked lists together
#returns the head of the combined list

    if not a:
        return b
    head = a
    # find the end of list a
    while a.next:
        a = a.next
    # link list b to the end of list a
    a.next = b
    return head
        
