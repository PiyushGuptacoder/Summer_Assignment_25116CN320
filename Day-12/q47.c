#include <stdio.h>
int print_fibonacci(int n){
    int a=0,b=1;
    printf("fibnacci series: ");
    printf("%d %d ",a,b);
    for (int i=3;i<=n;i++){
        int c=a+b;
        printf("%d ",c);
        a=b;
        b=c;
    }
}
int main(){
    int n;
    printf("Enter number of terms in fibonacci series: ");
    scanf("%d",&n);
    if (n==1){
        printf("The fibonacci series is: 0");}
    else if(n==2){
        printf("The fibonacci series is: 0 1");
        }
    else{
        print_fibonacci(n);

    }
    return 0;

}