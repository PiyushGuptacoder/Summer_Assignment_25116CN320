#include <stdio.h>
int sum(int n1,int n2){
    return n1+n2;
}
int main(){
    int n1,n2;
    printf("Enter two numbers to find its sum: ");
    scanf("%d%d",&n1,&n2);
    printf("The sum of two numbers is %d",sum(n1,n2));
    return 0;
}