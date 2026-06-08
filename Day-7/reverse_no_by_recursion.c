#include <stdio.h>
int reverse_no(int n1,int val){
    if(n1==0){
        return val;    
    }
    else{
        val=val*10+n1%10;
        return reverse_no(n1/10,val);
    }
}
int main(){
    int n;
    printf("enter the number to reverse it: ");
    scanf("%d",&n);
    printf("reverse of the number is %d",reverse_no(n,0));
    return 0;
}
