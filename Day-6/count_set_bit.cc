#include <stdio.h>
int count_set_bit(int n1){
    int c=0;
    while (n1>0){
        int r=n1%2;
        if (r==1){
            c++;
            }
        n1=n1/2;
    }
    return c;
}
int  main(){
    int n;
    printf("enter the number to count the set bit: ");
    scanf("%d",&n);
    printf("number of set bit: %d",count_set_bit(n));
    return 0;

}