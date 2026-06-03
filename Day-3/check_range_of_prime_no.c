#include <stdio.h>
int check_prime(int n1){
    printf("the prime nmber in the given range is:");
    for (int j=0;j<n1;j++){
        int c=0;
        for (int i=2;i<j;i++){
            if (j%i==0){
                c++;
            }
            else{
                continue;
            }
        }
        if (c==0){
            printf("%d ",j);
        }
    }
}
int main(){
    int n,c=0;
    printf("Enter the range of numbers  to check  it is prime or not: ");
    scanf("%d",&n);
    check_prime(n);
    return 0;

}