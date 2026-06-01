#include <stdio.h>
int main(){
    int n;
    int fact=1;
    printf("enter the no to find its factorial: ");
    scanf("%d",&n);
    if (n==0){
        printf("The factorial of 0 is 1");
    }
    else {
        for (int i=1;i<=n;i++){
            fact*=i;
            }
        printf("The factorial of %d is %d",n,fact);
    }
    return 0;
}