#include <stdio.h>
int power(int n1,int p1){
    int value=1;
    for (int i=1;i<=p1;i++)
    {
        value=value*n1;
    }
    printf("%d",value);

}
int main(){
    int n,p;
    printf("enter the number to find its power: ");
    scanf("%d",&n);
    printf("enter power: ");
    scanf("%d",&p);
    power(n,p);
    return 0;

}
