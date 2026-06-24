#include  <stdio.h>
int U_case(char str[]){
    int n=len_str(str);
    for(int i=0;i<n;i++){
        if(str[i]>=97 && str[i]<=122){
            str[i]=str[i]-32;
        }
    }
    printf("The string in upper case is %s",str);
    
}
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
    U_case(str);
    return 0;

}