#include <stdio.h>
int main(){
    int n,arr[100],target;
    printf("Enter the size of array: ");
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        printf("Enter the element %d: ",i+1);
        scanf("%d",&arr[i]);
    }
    printf("Enter the number to check its frequency in array: ");
    scanf("%d",&target);
    int c=0;
    for (int i=0;i<n;i++){
        if (arr[i]==target){
            c++;
        }
        if (c==0&& i==n-1){
            printf("\nThe number is not found");
        }
    }
    printf("The frequency of %d in the array is: %d",target,c);
    return 0;
}