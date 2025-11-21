//mergesort implementation in java with arrays
public class amergesort{
//1. dividing the array into two halves
//2. recursively sorting each half
//3. merging the two sorted halves back together
//time complexity: O(n log n) always
//space complexity: O(n) for temporary arrays
    public static void mergesort(int[] arr) {
        // base case: if array has 0 or 1 element it's already sorted
        if (arr.length <= 1) return;

        // divide: split the array into two halves
        int mid = arr.length / 2;
        int[] left = new int[mid];
        int[] right = new int[arr.length - mid];

        // copy elements into left and right arrays
        System.arraycopy(arr, 0, left, 0, mid);
        System.arraycopy(arr, mid, right, 0, arr.length - mid);

        // recursively sort both halves
        mergesort(left);
        mergesort(right);

        // conquer: merge the two sorted halves back into arr
        merge(arr, left, right);
    }
//merges two sorted arrays into one sorted array
//this method compares elements from both arrays and combines them in sorted order into the result array

    private static void merge(int[] result, int[] left, int[] right) {
        int i = 0, j = 0, k = 0;  // pointers for left right and result arrays

        // compare elements from both arrays and add the smaller one
        while (i < left.length && j < right.length) {
            if (left[i] < right[j])
                result[k++] = left[i++];
            else
                result[k++] = right[j++];
        }

        // add any remaining elements from left array
        while (i < left.length) result[k++] = left[i++];
        // add any remaining elements from right array
        while (j < right.length) result[k++] = right[j++];
    }
}
