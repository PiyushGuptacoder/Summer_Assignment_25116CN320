#include <stdio.h>
int rotate_right(int arr[],int n){
    int temp=arr[n-1];
    for (int i=n-2;i>=0;i--){
        arr[i+1]=arr[i];
        if (i==0){
            arr[0]=temp;
        }
    }
    // printf("The rotated array is: ");
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
    rotate_right(arr,n);
    return 0;
}