#include <stdio.h>
int fibonacci(int n1){
    if (n1==0){
        return 0;
    }
    else if (n1==1){
        return 1;
    }
    else{
        return fibonacci(n1-1)+fibonacci(n1-2);
    }
}
int main(){
    int n;
    printf("enter the number to find its fibonacci series: ");
    scanf("%d", &n);
    printf("fibonacci of %d is %d",n,fibonacci(n));
    return 0;
}