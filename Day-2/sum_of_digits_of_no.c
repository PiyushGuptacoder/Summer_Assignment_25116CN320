#include <stdio.h>
int main(){
    int n,r;
    int sum=0;
    printf("enter the number to find its sum of digits: ");
    scanf("%d",&n);
    while(n>0){
        r=n%10;
        n=n/10;
        sum+=r;
    }
    printf("the sum of digits of the no is:%d",sum);
    return 0;


}
