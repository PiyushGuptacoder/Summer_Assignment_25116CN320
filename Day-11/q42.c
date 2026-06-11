#include <stdio.h>
int max_num(int n1,int n2){
    if(n1>n2){
        return n1;
    }
    
    else{
        return n2;

    }
}
int main(){
        int n1,n2;
        printf("Enter two numbers to find the maximum number: ");
        scanf("%d%d",&n1,&n2);
        if (n1==n2){
            printf("Both numbers are equal");
        }
        else{
            printf("The maximum is %d",max_num(n1,n2) );
        }
        return 0; 
}
