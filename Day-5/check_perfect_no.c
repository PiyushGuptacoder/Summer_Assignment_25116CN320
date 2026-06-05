#include <stdio.h>
int check_perfectno(int n1){
    int sum=0;
    for (int i=1;i<n1;i++){
        if (n1%i==0){
            sum+=i;
            }
    }
    return sum;
}
int main(){
    int n;
    printf("Enter  the number to check it iss perfect or not: ");
    scanf("%d",&n);
    if (n==0){
        printf("The given number is not a perfect number");
    }
    else{
        if (check_perfectno(n)==n){
            printf("the given number is perfect number");
        }
        else{
            printf("the given number is not a perfect number");
        }
    }


}