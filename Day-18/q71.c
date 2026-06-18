#include <stdio.h>
int binarysearch(int arr[],int n,int target){
    int l=0,high=n-1;
    while(l<=high){
        int mid=(l+high)/2;
        if (arr[mid]==target){
            printf("The target value is found at index: %d",mid);
            return mid;
        }
        else if(arr[mid]<target){
            l=mid+1;
        }
        else{
            high=mid-1;}
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
    printf("Enter the target value: ");
    scanf("%d",&target);
    binarysearch(arr,n,target);
    return 0;
}