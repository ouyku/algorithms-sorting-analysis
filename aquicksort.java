//quicksort implementation in java with arrays
public class aquicksort {

    public static void quicksort(int[] arr, int low, int high) {
        if (low < high) {
            // partition the array and get the pivot index
            int p = partition(arr, low, high);
            // recursively sort elements before and after partition
            quicksort(arr, low, p - 1);
            quicksort(arr, p + 1, high);
        }
    }
    private static int partition(int[] arr, int low, int high) {
        // choose the last element as pivot
        int pivot = arr[high];
        int i = low - 1;  // index of smaller element (indicates right position of pivot)

        // traverse through the array and compare each element with pivot
        for (int j = low; j < high; j++) {
            // if current element is smaller than or equal to pivot
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        // place pivot in its correct position
        swap(arr, i + 1, high);
        return i + 1;
    }
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
