/**
 * Created BY - YASAS SANDEEPA
 * Undergraduate - Bsc(Hons) in Information Technology #17
 * University of Moratuwa
 * Sri Lanka
 */
public class BubbleSort {

    void sort(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
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
         BubbleSort bubbleSort = new BubbleSort();
         int arr[] = {64, 34, 25, 12, 22, 11, 90};
         System.out.println("====Array without Sorting=====");
         bubbleSort.print(arr);
         System.out.println("==============================");
         System.out.println();
         bubbleSort.sort(arr);
         System.out.println("==========Sorted array========");
         bubbleSort.print(arr);
         System.out.println("==============================");
     }

    public static void main(String args[]) {
        BubbleSort.test();

    }
}
