#include <stdio.h>
int no_pyramid(int n1){
    for(int i=1;i<=n1;i++){
        for (int k=1;k<i;k++){
            printf(" ");
        }
        for (int j=1;j<=(2*(n1-i+1)-1);j++){
            printf("*");
        }
        printf("\n");
    }
}
int main(){
    int n;
    printf("Enter the number of rows in pyramid: ");
    scanf("%d",&n);
    no_pyramid(n);
    return 0;
}
