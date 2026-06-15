#include <stdio.h>
int rotate_left(int arr[],int n){
    int temp=arr[0];
    for (int i=0;i<n;i++){
        // int temp=arr[i];
        arr[i]=arr[i+1];
        if (i==n-1){
            arr[i]=temp;
        }
    }
    printf("the rotated array is: ");
    for (int i=0;i<n;i++){
        printf("%d\t",arr[i]);
    }
}
int main(){
    int n,arr[100],target;
    printf("Enter the size of array: ");
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        printf("Enter the element %d: ",i+1);
        scanf("%d",&arr[i]);
    }
    rotate_left(arr,n);
    return 0;
}