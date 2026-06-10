#include <stdio.h>
int no_pyramid(int n1){
    for(int i=1;i<=n1;i++){
        for (int k=1;k<=n1-i;k++){
            printf(" ");
        }
        for (int p=1;p<=i;p++){
            printf("%d",p);
        }
        for (int q=i-1;q>=1;q--){
            printf("%d",q);
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
