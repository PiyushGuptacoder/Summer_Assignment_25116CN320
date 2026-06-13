#include <stdio.h>
int main(){  
    int n,arr[100];
    printf("Enter the size of array: ");
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        printf("Enter the element %d: ",i+1);
        scanf("%d",&arr[i]);
    }
    printf("The elements of array are: ");
    for (int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }

    
}