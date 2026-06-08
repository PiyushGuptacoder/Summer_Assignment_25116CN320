#include <stdio.h>
int no_pyramid(int n1){
    for(int i=1;i<=n1;i++){
        for (int j=1;j<=i;j++){
            printf("%d",i);
        }
        printf("\n");
    }
}
int main(){
    int n;
    printf("Enter the number of rows in triangle: ");
    scanf("%d",&n);
    no_pyramid(n);
    return 0;
}