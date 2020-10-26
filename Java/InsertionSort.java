/**
 * Created BY - YASAS SANDEEPA
 * Undergraduate - Bsc(Hons) in Information Technology #17
 * University of Moratuwa
 * Sri Lanka
 */
public class InsertionSort {


    void sort(int arr[]) {
        int n = arr.length;
        for (int i = 1; i < n; ++i) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }


    void print(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void test(){
        InsertionSort insertionSort = new InsertionSort();
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("====Array without Sorting=====");
        insertionSort.print(arr);
        System.out.println("==============================");
        System.out.println();
        insertionSort.sort(arr);
        System.out.println("==========Sorted array========");
        insertionSort.print(arr);
        System.out.println("==============================");
    }


    public static void main(String args[]) {
        InsertionSort.test();
    }
}
