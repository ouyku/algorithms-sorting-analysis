#mergesort implementation in python with linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def mergesort_linked_list(head):
    # base case: if list is empty or has one element it's already sorted
    if not head or not head.next:
        return head

    # split the list into two halves
    mid = split(head)
    left = mergesort_linked_list(head)   # sort left half
    right = mergesort_linked_list(mid)   # sort right half

    # merge the two sorted halves
    return merge_lists(left, right)

def split(head):
    slow = head
    fast = head.next
    
    # move fast pointer twice as fast as slow pointer
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # split the list at the middle
    mid = slow.next
    slow.next = None  # break the connection
    return mid

def merge_lists(a, b):
    # create a dummy node to simplify the merging process
    dummy = Node(0)
    tail = dummy

    # compare elements from both lists and link the smaller one
    while a and b:
        if a.val < b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    # link any remaining elements
    tail.next = a if a else b
    return dummy.next
