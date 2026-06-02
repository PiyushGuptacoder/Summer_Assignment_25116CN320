#include <stdio.h>
int main(){
    int n,r;
    int product=1;
    printf("enter a number: ");
    scanf("%d",&n);
    if (n==0){
        printf("product of the digit is: 0");
    }
    else{

        while(n>0){
            r=n%10;
            n/=10;
            product*=r;

        }
        printf("product of digit is: %d",product);
    }
    return 0;
}