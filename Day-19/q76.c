#include <stdio.h>
int sum_diagonal(int m1, int n1,int mat[][n1]) {
    int sum = 0;
    for (int i = 0; i < m1; i++) {
        for (int j = 0; j < n1; j++) {
            if(i==j){
                sum+=mat[i][j];
            }
        }
    }
    printf("The sum of the diagonal elements is: %d\n", sum);
    return sum;
}

int main(){
    int m1,n1,m2,n2;
    printf("Enter the size of matrix 1: ");
    scanf("%d%d",&m1,&n1);
    
    int mat1[m1][n1];
    for (int i=0;i<m1;i++){
        for (int j=0;j<n1;j++){
            printf("Enter the element (%d,%d) of matrix 1: ",i,j);
            scanf("%d",&mat1[i][j]);
        }
    }
    sum_diagonal(m1,n1,mat1);
    return 0;

}