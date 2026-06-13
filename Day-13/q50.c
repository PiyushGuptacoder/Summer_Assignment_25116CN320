#include <stdio.h>
int main(){
    int n,arr[100];
    printf("Enter the size of array: ");
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        printf("Enter the element %d: ",i+1);
        scanf("%d",&arr[i]);
    }
    int sum=0;
    for (int i=0;i<n;i++){
        sum+=arr[i];
    }
    printf("The sum of the array elements is: %d",sum);
    printf("\nthe average of array elments is: %f", (float)sum/n);
}

 