#include <stdio.h>
int selectionsort(int arr[],int n){
    for(int i=0;i<n-1;i++){
        int m=i;
        for (int j=i+1;j<n;j++){
            if (arr[j]<arr[m]){
                m=j;
            }
        }
        int temp=arr[i];
        arr[i]=arr[m];
        arr[m]=temp;
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
    selectionsort(arr,n);
    printf("The sorted array is: ");
    for (int i=0;i<n;i++){
        printf("%d\t",arr[i]);
    }
    return 0;
}