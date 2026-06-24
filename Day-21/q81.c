#include  <stdio.h>
int len_str(char str[]){
    int i=0;
    while(str[i]!='\0'){
        i++;
    }
    return i;
}
int main(){
    char str[10];
    printf("Enter the string ");
    scanf("%s",str);
    printf("The length of string is %d",len_str(str));
    return 0;

}