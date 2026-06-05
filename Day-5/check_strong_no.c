#include <stdio.h>
int factorial(int n1){
    if (n1==0||n1==1){
        return 1;
    }
    else{
        return n1*factorial(n1-1);
    }
}
int check_strong_no(int n1){
    int number=0;
    int r;
    while (n1!=0){
        r=n1%10;
        number+=factorial(r);
        n1/=10;
    }
    return number;
}
int main(){
    int n;
    printf("Enter the  number to check it is strong or not: ");
    scanf("%d",&n);
    if (n==0){
        printf("The given number is not a strong number");
    }
    else if(check_strong_no(n)==n){
        printf("The number is a strong number.");
    }
    else{
        printf("The number is not a strong number.");
    }
}