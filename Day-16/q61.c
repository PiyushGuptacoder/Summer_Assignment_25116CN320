#include <stdio.h>
int missing_value(int arr[],int n){
    int sum=(n*(n+1))/2;
    int sum1=0;
    for (int i=0;i<n-1;i++){
        sum1+=arr[i];
    }
    return sum-sum1;
}

int main(){
    int n,arr[100],target;
    printf("Enter the size of array: ");
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        printf("Enter the element %d: ",i+1);
        scanf("%d",&arr[i]);
    }
    printf("The missing value in the array is: %d",missing_value(arr,n));
    return 0;
}