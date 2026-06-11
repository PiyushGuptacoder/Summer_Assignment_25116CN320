#include <stdio.h>
int check_prime(int n1){
    int c=0;
    for (int i=2;i<n1;i++){
        if (n1%i==0){
            c++;
        }
        else{
            continue;
        }
    }
    if (c==0){
        printf("The given number  is  prime");
    }
    else{
        printf("The given number is not prime");
    }
}
int main(){
    int n,c=0;
    printf("Enter the number to check  it is prime or not: ");
    scanf("%d",&n);
    if (n==0||n==1){
        printf("The given number is not prime");
    }
    else{
    check_prime(n);
    }
    return 0;

}