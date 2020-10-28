#include<stdio.h>

void merge(int array[], int l, int m, int r) 
{ 
    int i, j, k; 
    int num1 = m - l + 1; 
    int num2 = r - m; 
 
    /* create temp arrays */
    int Left[num1], Right[num2]; 
 
    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < num1; i++) 
        Left[i] = array[l + i]; 
    for (j = 0; j < num2; j++) 
        Right[j] = array[m + 1 + j]; 

    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray 
    j = 0; // Initial index of second subarray 
    k = l; // Initial index of merged subarray 
    while (i < num1 && j < num2) { 
        if (Left[i] <= Right[j]) { 
            array[k] = Left[i]; 
            i++; 
        } 
        else { 
            array[k] = Right[j]; 
            j++; 
        } 
        k++; 
    } 
 
    /* Copy the remaining elements of L[], if there 
    are any */
    while (i < num1) { 
        array[k] = Left[i]; 
        i++; 
        k++; 
    } 
 
    /* Copy the remaining elements of R[], if there 
    are any */
    while (j < num2) { 
        array[k] = Right[j]; 
        j++; 
        k++; 
    } 
} 
 
/* l is for left index and r is right index of the 
sub-array of arr to be sorted */
void mergeSort(int array[], int l, int r) 
{ 
    if (l < r) { 
        // Same as (l+r)/2, but avoids overflow for 
        // large l and h 
        int m = l + (r - l) / 2; 
 
        // Sort first and second halves 
        mergeSort(array, l, m); 
        mergeSort(array, m + 1, r); 
 
        merge(array, l, m, r); 
    } 
} 
 
void printArray(int arr[], int size){
    int x; 
    for (x = 0; x < size; x++)
        printf("%d ", arr[x]);
    printf("\n");
}


int main(){
    int n = 0;
    printf("Enter number of elements: ");
    scanf("%d", &n); 
    int array[n];

    printf("Enter elements\n");
    for(int i = 0; i < n; i++)
        scanf("%d", &array[i]);
	n = sizeof(array)/sizeof(array[0]);

    mergeSort(array, 0, n - 1); 
    printf("\nSorted array is :");
    printArray(array, n);
    return 0;
}