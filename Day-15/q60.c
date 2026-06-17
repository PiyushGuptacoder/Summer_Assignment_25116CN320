#include <stdio.h>

void moveZeroes(int arr[], int n) {
    int j= 0; 
    for (int i = 0; i < n; i++) {
        if (arr[i] != 0) {
            arr[j++] = arr[i];
            // j++;
        }
    }
    while (j < n) {
        arr[j++] = 0;
    }
    printf("array after moving zeroes: ");
    for (int i=0;i<n;i++){
        printf("%d\t",arr[i]);
    }
}

int main() {
    int arr[100];
    int n;
    printf("Enter the size of array: ");
    scanf("%d",&n);

    for (int i = 0; i < n; i++) {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &arr[i]);
    }
    moveZeroes(arr, n);
    return 0;
}
