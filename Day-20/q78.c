#include <stdio.h>
int isSymmetric(int n, int mat[][n]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (mat[i][j] != mat[j][i]) {
                return 0; 
            }
        }
    }
    return 1; 
}
int main(){
    int m1,n1;
    printf("Enter the size of matrix 1: ");
    scanf("%d%d",&m1,&n1);
    if(m1!=n1){
        printf("The matrix is not square matrix\n");
    }
    else{
        int mat1[m1][n1];
        for (int i=0;i<m1;i++){
            for (int j=0;j<n1;j++){
                printf("Enter the element (%d,%d) of matrix 1: ",i,j);
                scanf("%d",&mat1[i][j]);
            }
        }
    
    
        if (isSymmetric(n1,mat1)){
            printf("The matrix is symmetric\n");
        }
        else{
            printf("The matrix is not symmetric\n");
        }
    }
}