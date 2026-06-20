#include <stdio.h>
int multiplyMatrices(int m1, int n1,int n2, int m2, int A[][n1], int B[][n2], int C[][n2]) {
    if (m1!=n2){
        printf("Matrices cannot be multiplied");
        return 0;
    }
    else{
        for (int i = 0; i < m1; i++) {
            for (int j = 0; j < n2; j++) {
                C[i][j] = 0;
                for (int k = 0; k < n1; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
    }
    printf("The product of the matrices is: \n");
    for(int i=0;i<m1;i++){
        for(int j=0;j<n2;j++){
            printf("%d ",C[i][j]);
        }
        printf("\n");
    }
}
int main(){
    int m1,n1,m2,n2;
    printf("Enter the size of matrix 1: ");
    scanf("%d%d",&m1,&n1);
    printf("\nEnter the size of matrix 2: ");
    scanf("%d%d",&m2,&n2);
    int mat1[m1][n1],mat2[m2][n2];
    for (int i=0;i<m1;i++){
        for (int j=0;j<n1;j++){
            printf("\nEnter the element (%d,%d) of matrix 1: ",i,j);
            scanf("%d",&mat1[i][j]);
        }
    }
    for (int i=0;i<m2;i++){
        for (int j=0;j<n2;j++){
            printf("\nEnter the element (%d,%d) of matrix 2: ",i,j);
            scanf("%d",&mat2[i][j]);
        }
    }
    int mat3[m1][n2];
    multiplyMatrices(m1,n1,n2,m2,mat1,mat2,mat3);
}