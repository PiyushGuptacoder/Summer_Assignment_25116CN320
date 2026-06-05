#include <stdio.h>
int find_gcd(int a,int b){
    while(b!=0)
        {int temp=a;
        a=b;
        b=temp%b;
    }
    return a;
}
int find_lcm(int p, int q) {
    return (p * q) / find_gcd(p, q);
}
int main(){
    int n1,n2;
    printf("Enter two numbers to find lcm: ");
    scanf("%d %d",&n1,&n2);
    printf("lcm of %d and %d is %d",n1,n2,find_lcm(n1,n2));
    return 0;
}