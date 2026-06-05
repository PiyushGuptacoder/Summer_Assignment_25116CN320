#include <stdio.h>
int find_gcd(int a,int b){
    while(b!=0)
        {int temp=a;
        a=b;
        b=temp%b;
    }
    return a;
}

int main(){
    int n1,n2;
    printf("Enter two numbers to find gcd: ");
    scanf("%d %d",&n1,&n2);
    printf("GCD of %d and %d is %d",n1,n2,find_gcd(n1,n2));
}