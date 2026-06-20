#include <stdio.h>

int main(){
    int m1,n1,m2,n2;
    printf("Enter the size of matrix 1: ");
    scanf("%d%d",&m1,&n1);
    printf("Enter the size of matrix 2: ");
    scanf("%d%d",&m2,&n2);
    int mat1[m1][n1],mat2[m2][n2];
    for (int i=0;i<m1;i++){
        for (int j=0;j<n1;j++){
            printf("Enter the element (%d,%d) of matrix 1: ",i,j);
            scanf("%d",&mat1[i][j]);
        }
    }
    for (int i=0;i<m2;i++){
        for (int j=0;j<n2;j++){
            printf("Enter the element (%d,%d) of matrix 2: ",i,j);
            scanf("%d",&mat2[i][j]);
        }
    }

}