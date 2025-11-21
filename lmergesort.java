//mergesort implementation in java with linked list
public class lmergesort {
    // node class for linked list
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) {
            this.val = val;
            this.next = null;
        }
    }

//1. splitting the list into two halves
//2. recursively sorting each half
//3. merging the two sorted halves back together

//time complexity: O(n log n) always
//space complexity: O(log n) for recursion stack

    public static ListNode mergesort(ListNode head) {
        // base case: if list is empty or has one element it's already sorted
        if (head == null || head.next == null) {
            return head;
        }

        // split the list into two halves
        ListNode mid = split(head);
        ListNode left = mergesort(head);   // sort left half
        ListNode right = mergesort(mid);   // sort right half

        // merge the two sorted halves
        return merge(left, right);
    }

//splits a linked list into two halves
//uses two pointers: slow (moves 1 step) and fast (moves 2 steps)
//when fast reaches the end, slow is at the middle
    private static ListNode split(ListNode head) {
        ListNode slow = head;
        ListNode fast = head.next;
        
        // move fast pointer twice as fast as slow pointer
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // split the list at the middle
        ListNode mid = slow.next;
        slow.next = null;  // break the connection
        return mid;
    }

//merges two sorted linked lists into one sorted linked list
//compares elements from both lists and links them in sorted order

    private static ListNode merge(ListNode a, ListNode b) {
        // create a dummy node to simplify the merging process
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;

        // compare elements from both lists and link the smaller one
        while (a != null && b != null) {
            if (a.val < b.val) {
                tail.next = a;
                a = a.next;
            } else {
                tail.next = b;
                b = b.next;
            }
            tail = tail.next;
        }

        // link any remaining elements
        tail.next = (a != null) ? a : b;
        return dummy.next;
    }
}
