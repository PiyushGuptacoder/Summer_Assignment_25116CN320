#include <stdio.h>
int main(){
    int n,arr[100],target;
    printf("Enter the size of array: ");
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        printf("Enter the element %d: ",i+1);
        scanf("%d",&arr[i]);
    }
    printf("Enter the number to find in array: ");
    scanf("%d",&target);
    for (int i=0;i<n;i++){
        if (arr[i]==target){
            printf("The number %d is found at index %d",target,i);
            break;
        }
        if (i==n-1){
            printf("The number is not found",target);
        }
    }
    
    return 0;
}