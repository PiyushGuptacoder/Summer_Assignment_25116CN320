#include <stdio.h>
#include <string.h>
void remove_spaces(char str[]){
    for(int i=0;i<strlen(str);i++){
        if(str[i]==' '){
            str[i]='\0';
        }
    }
    puts(str);
}
int main(){
    char str[100];
    printf("Enter the string\n");
    gets(str);
    puts(str);
    remove_spaces(str);
    return 0;
}