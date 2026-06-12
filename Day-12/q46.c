#include <stdio.h>
#include <math.h>
int no_of_digit(int n1){
    int count =0;
    while(n1>0){
        n1/=10;
        count++;
    }
    return count;
}
int check_armstrong(int n2,int n){
    int r,n3=0;

    while(n2>0){
        r=n2%10;
        // printf("r%d",r);
        n2/=10;
        n3=n3+pow(r,no_of_digit(n));
        }
        return n3;
}
int main(){
    int n;
    printf("Enter the number upto which to find armsstrong numbers: ");
    scanf("%d",&n);
    for (int i=1;i<=n;i++){
        if (check_armstrong(i,i)==i){
            printf("%d is an armstrong number\n", i);
        }
        // else{
        //     printf("The given number is not armstrong");
        // }
    }

}