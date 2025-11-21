//quicksort implementation in java with linked list

public class lquicksort {
    
    // node class for linked list
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) {
            this.val = val;
            this.next = null;
        }
    }


//1. choosing a pivot element
//2. partitioning the list into elements less than equal to and greater than the pivot
//3. recursively sorting the partitions

//time complexity: O(n log n) average - O(n²) worst case
//space complexity: O(log n) average for recursion stack
    public static ListNode quicksort(ListNode head) {
        // base case: if list is empty or has one element it's already sorted
        if (head == null || head.next == null) {
            return head;
        }
        // partition the list around the pivot
        PartitionResult result = partition(head);
        // recursively sort the less and greater partitions
        ListNode less = quicksort(result.less);
        ListNode greater = quicksort(result.greater);
        // concatenate: less + equal + greater
        ListNode sorted = concatenate(less, result.equal);
        sorted = concatenate(sorted, greater);
        return sorted;
    }


//partitions a linked list into three parts based on a pivot value
//returns three lists
//less: elements smaller than pivot
//equal: elements equal to pivot
//greater: elements greater than pivot
    private static PartitionResult partition(ListNode head) {
        if (head == null || head.next == null) {
            return new PartitionResult(head, null, null);
        }

        // choose first element as pivot
        int pivot = head.val;
        
        // create three lists to hold partitioned elements
        ListNode lessHead = null, lessTail = null;
        ListNode equalHead = null, equalTail = null;
        ListNode greaterHead = null, greaterTail = null;

        // traverse the list and partition elements
        ListNode current = head;
        while (current != null) {
            ListNode next = current.next;
            current.next = null;  // disconnect node
            
            if (current.val < pivot) {
                if (lessHead == null) {
                    lessHead = lessTail = current;
                } else {
                    lessTail.next = current;
                    lessTail = current;
                }
            } else if (current.val == pivot) {
                if (equalHead == null) {
                    equalHead = equalTail = current;
                } else {
                    equalTail.next = current;
                    equalTail = current;
                }
            } else {
                if (greaterHead == null) {
                    greaterHead = greaterTail = current;
                } else {
                    greaterTail.next = current;
                    greaterTail = current;
                }
            }
            current = next;
        }

        return new PartitionResult(lessHead, equalHead, greaterHead);
    }

//concatenates two linked lists together
//returns the head of the combined list
    private static ListNode concatenate(ListNode a, ListNode b) {
        if (a == null) {
            return b;
        }
        ListNode head = a;
        // find the end of list a
        while (a.next != null) {
            a = a.next;
        }
        // link list b to the end of list a
        a.next = b;
        return head;
    }

//helper class to return three lists from partition function

    private static class PartitionResult {
        ListNode less;
        ListNode equal;
        ListNode greater;
        
        PartitionResult(ListNode less, ListNode equal, ListNode greater) {
            this.less = less;
            this.equal = equal;
            this.greater = greater;
        }
    }
}
