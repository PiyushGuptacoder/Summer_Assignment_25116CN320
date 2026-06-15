#include <stdio.h>
int reverse(int arr[],int n){
    int temp;
    for (int i=0;i<n/2;i++){
        temp=arr[i];
        arr[i]=arr[n-1-i];
        arr[n-1-i]=temp;
    }
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
    reverse(arr,n);
    return 0;
}