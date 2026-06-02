#include <stdio.h>
int main(){
    int n,r;
    int rev=0;
    printf("enter the no to reverse it: ");
    scanf("%d",&n);
    while (n>0){
        r=n%10;
        n=n/10;
        rev=rev*10+r;
    }
    printf("the reverse of the no is: %d",rev);
    return 0;

} 