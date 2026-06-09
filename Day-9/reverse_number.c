#include <stdio.h>
int half_pyramid(int n1){
    for (int i=1;i<=n1;i++){
        for (int j=1;j<=n1+1-i;j++){
            printf("%d",j);
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