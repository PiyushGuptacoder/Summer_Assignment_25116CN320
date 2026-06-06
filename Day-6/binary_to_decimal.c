#include <stdio.h>
#include <math.h>
int binary_to_decimal(int n1){
    int r=0,i=0,dec=0;
    while(n1>0){
    r=n1%10;
    n1=n1/10;
    dec=dec+pow(2,i)*r;
    i++;
    }
    printf("Decimal:%d",dec);
}
int check_binary(int n2){
    int r,a=0;
    while(n2>0){
        r=n2%10;
        n2=n2/10;
        if (r!=0 &&r!=1){
            a=1;
            break;
            }
        }
    return a;
}
int main(){
    int n;
    printf("Enter the binary number to convert into decimal number:  ");
    scanf("%d",&n);

    if (check_binary(n)==0){
        binary_to_decimal(n);
    } 
    else {
        printf("Invalid binary number.");
    }
    return 0;
}