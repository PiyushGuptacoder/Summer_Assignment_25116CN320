#include <stdio.h>
int add_matrix(int m1,int n1,int n2,int m2,int mat1[][n1],int mat2[][n2],int mat3[][n2]){
    if (m1!=m2 || n1!=n2){
        printf("Matrices cannot be added");
    
    }
    for (int i=0;i<m1;i++){
        for (int j=0;j<n1;j++){
            mat3[i][j]= mat1 [i][j]+ mat2[i][j];
        }
    }
    printf("The sum of the matrices is: \n");
    for (int i=0;i<m1;i++){
        for (int j=0;j<n1;j++){
            printf("%d ",mat3[i][j]);
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
    int mat1[m1][n1],mat2[m2][n2],mat3[m2][n2];
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
    add_matrix(m1,n1,n2,m2,mat1,mat2,mat3);

}