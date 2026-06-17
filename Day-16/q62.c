#include <stdio.h>
int max_frequency(int arr[],int n){
    // int c=0;
    int c[1000]={0};
    for (int i=0;i<n;i++){
            c[arr[i]]++;
            }
        
    
    int max=c[0],element;
    for (int i=0;i<1000;i++){
        if (c[i]>max){
            max=c[i];
            element=i;
        }
    }
    return element;
}
int main(){
    int n,arr[100],target;
    printf("Enter the size of array: ");
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        printf("Enter the element %d: ",i+1);
        scanf("%d",&arr[i]);
    }
    printf("The maximum frequency of the elements in the array is: %d",max_frequency(arr,n));
    return 0;
}