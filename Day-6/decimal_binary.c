#include <stdio.h>
int decimal_to_binary(int n1){
    int bin[32],i=0;
    while (n1>0){
        bin[i]=n1%2;
        n1=n1/2;
        i++;
    }
    printf("binary: ");
    for (int j=i-1;j>=0;j--){
    printf("%d",bin[j]);
    }
}
int main(){
    int n;
    printf("Enter the number to covert to binary: ");
    scanf("%d",&n);
    decimal_to_binary(n);
    return 0;
}
    

