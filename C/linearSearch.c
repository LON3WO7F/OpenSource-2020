#include <stdio.h>
 
#define N 100

int search(int arr[], int n, int x)
{
    int i;
    for (i = 0; i < n; i++)
        if (arr[i] == x)
            return i;
    return -1;
}
 
// Driver code
int main(void)
{
    int arr[N];
    printf("Enter size of array: ");
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    printf("Enter element to be searched: ");
    int x;
    scanf("%d", &x);
    n = sizeof(arr) / sizeof(arr[0]);
   
    // Function call
    int result = search(arr, n, x);
    (result == -1)
        ? printf("Element is not present in array\n")
        : printf("Element is present at index %d\n", result);
    return 0;
}