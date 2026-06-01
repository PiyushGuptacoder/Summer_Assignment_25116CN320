#include <stdio.h>
int main(){
    int n;
    int sum = 0;
    printf("enter a number: ");
    scanf("%d",&n);
    for (int i=1;i<=n;i++) {
        sum+=i;
        }
    printf("the sum of first %d natural number is %d",n,sum);
    return 0;
}