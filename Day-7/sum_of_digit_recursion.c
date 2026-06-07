#include <stdio.h>
int sum_of_digit(int n1){
    if(n1==0){
        return 0;

    }
    else{
        return sum_of_digit(n1/10)+n1%10;
    }

}
int main(){
    int n;
    printf("enter the number to find the sum of its digit: ");
    scanf("%d", &n);
    printf("sum of digit of %d is %d", n, sum_of_digit(n));
    return 0;
}