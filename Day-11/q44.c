#include <stdio.h>
int factorial(int n){

    int f=1;
    if (n==0){
        return 1;
    }
    for (int i=1;i<=n;i++){
        f*=i;

    }
    return f;
}
int main(){
    int n;
    int fact=1;
    printf("enter the no to find its factorial: ");
    scanf("%d",&n);
    printf("The factorial of %d is %d",n,factorial(n));
    return 0;
}