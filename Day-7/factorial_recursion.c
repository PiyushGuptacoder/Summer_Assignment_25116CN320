#include <stdio.h>
int factorial(int n1){
    if (n1==0||n1==1){
        return 1;
    }
    else{
        return n1*factorial(n1-1);
    }
}
int main(){
    int n;
    printf("enter the number to find its factorial: ");
    scanf("%d", &n);
    if(n<0){
        printf("Factorial is not defined.");
        
    }
    else{
        printf("factorial of %d is %d", n, factorial(n));
    }
    return 0;
}