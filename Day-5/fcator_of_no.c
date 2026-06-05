#include <stdio.h>
int find_factor(int n1){
    printf("factor of %d is ",n1);
    for (int i=1;i<=n1;i++){
        if(n1%i==0){
            printf("%d ",i);
        }
    }
}
int main(){
    int n;
    printf("Enter the number to find its factors: ");
    scanf("%d",&n);
    if (n==0){
        printf("No factors exist");
    }
    else{
        find_factor(n);
    }
    
}
