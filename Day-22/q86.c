#include <stdio.h>
#include <string.h>
int count_words(char str[]){
    int c=0;
    for(int i=0;i<strlen(str);i++){
        if(str[i]==' '){
            c++;
        }
    }
    return c+1;
}
int main(){
    char str[100];
    printf("Enter the string\n");
    gets(str);
    printf("The number of words in the string is %d", count_words(str));
    return 0;
}