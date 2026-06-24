#include <stdio.h>
int sum_row(int n,int mat[][n]){
    int sum=0;
    for (int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            sum+=mat[i][j];
            
        }
        printf("the sum of elements of row%d is %d\n",i+1,sum);
    }
    
}

int main(){
    int m1,n1;
    printf("Enter the size of matrix 1: ");
    scanf("%d%d",&m1,&n1);
    
    int mat1[m1][n1];
    for (int i=0;i<m1;i++){
        for (int j=0;j<n1;j++){
            printf("Enter the element (%d,%d) of matrix 1: ",i,j);
            scanf("%d",&mat1[i][j]);
        }
    }
    sum_row(n1,mat1);
    return 0;

}