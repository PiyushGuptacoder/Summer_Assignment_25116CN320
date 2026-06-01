#include <stdio.h>
int main(){
    int n;
    int count=0;
    printf("Enter the number to count digit: ");
    scanf("%d",&n);
    while(n>0){
        n=n/10;
        count++;
    }
    printf("The number of digit in the given number is %d",count);
    return 0;

}