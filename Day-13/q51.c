#include <stdio.h>
int largest_no(int arr[],int n){
    int max=arr[0];
    for (int i=0;i<n;i++){
        if (arr[i]>max){
            max=arr[i];
        }
    }
    return max;
}
int smallest_no(int arr[],int n){
    int min=arr[0];
    for (int i=0;i<n;i++){
        if (arr[i]<min){
            min=arr[i];
        }
    }
    return min;
}
int main(){  
    int n,arr[100];
    printf("Enter the size of array: ");
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        printf("Enter the element %d: ",i+1);
        scanf("%d",&arr[i]);
    }
    printf("The largest element of array is: %d",largest_no(arr,n));
    printf("The smallest element of array is: %d",smallest_no(arr,n));
    return 0;
    
}