#include <stdio.h>
int half_pyramid(int n1){
    for (int i=1;i<=n1;i++){
        for (int j=i;j<=n1;j++){
            printf("*");
        }
        printf("\n");
    }
}
int main(){
    int n;
    printf("Enter the number of rows for half pyramid: ");
    scanf("%d",&n);
    half_pyramid(n);
    return 0;
}