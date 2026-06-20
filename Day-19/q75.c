#include <stdio.h>
int transpose(int m1, int n1, int mat[][n1], int trans[][m1]) {
    for (int i = 0; i < m1; i++) {
        for (int j = 0; j < n1; j++) {
            trans[j][i] = mat[i][j];
        }
    }
    printf("The transpose of the matrix is: \n");
        for (int i=0;i<n1;i++){
            for (int j=0;j<m1;j++){
                printf("%d ",trans[i][j]);
            }
            printf("\n");
        }
}

int main(){
    int m1,n1,m2,n2;
    printf("Enter the size of matrix 1: ");
    scanf("%d%d",&m1,&n1);
    
    int mat1[m1][n1],trans[n1][m1];
    for (int i=0;i<m1;i++){
        for (int j=0;j<n1;j++){
            printf("\nEnter the element (%d,%d) of matrix 1: ",i,j);
            scanf("%d",&mat1[i][j]);
        }
    }
    transpose(m1,n1,mat1,trans);
    return 0;
}