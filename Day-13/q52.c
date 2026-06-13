#include <stdio.h>
int even_or_odd(int arr[],int n){
    int even=0,odd=0;
    for (int i=0;i<n;i++){
        if (arr[i]%2==0){
            even++;
        }
        else{
            odd++;
        }
    }
    printf("The number of even elements in array are: %d\n",even);
    printf("The number of odd elements in array are: %d",odd);
}
int main(){  
    int n,arr[100];
    printf("Enter the size of array: ");
    scanf("%d",&n);
    for (int i=0;i<n;i++){
        printf("Enter the element %d: ",i+1);
        scanf("%d",&arr[i]);
    }
    even_or_odd(arr,n);
    return 0;
}