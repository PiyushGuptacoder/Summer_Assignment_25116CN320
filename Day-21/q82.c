#include  <stdio.h>
#include <string.h>
int len_str(char str[]){
    int i=0;
    while(str[i]!='\0'){
        i++;
    }
    return i;
}
void rev_str(char str[]){
    int i,len=len_str(str);
    printf("\nThe reverse of string is ");
    for(i=len;i>=0;i--){
        printf("%c",str[i]);
    }
}
int main(){
    char str[10];
    printf("Enter the string ");
    scanf("%s",str);
    rev_str(str);
    return 0;

}