#include <stdio.h>
int main(){
    int n,arr[100],target;
    printf("Enter the size of array: ");
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        printf("Enter the element %d: ",i+1);
        scanf("%d",&arr[i]);
    }
    int max=arr[0];
    int max2=arr[0];

    for(int i=0;i<n;i++){
        if (arr[i]>max){
            max=arr[i];
        }
    }
    for (int j=0;j<n;j++){
        if(max>arr[j]&&arr[j]>max2){
            max2=arr[j];
        }
    }
    printf("The second largest element in the array is: %d",max2);
    return 0;
}