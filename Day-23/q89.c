#include <stdio.h>
#include <string.h>
int non_repeating_char(char str[]){
    int n=strlen(str);
    for(int i=0;i<n;i++){
        int c=0;
        for (int j=0;j<n;j++){
            if (str[i]==str[j] && i!=j){
                c++;
                break;
            }
            // else if(i!=j){
            //     printf("The first non-repeating character is %c",str[i]);
            //     return 0;
            //     break;


            }
        if(c==0){
            printf("The first non-repeating character is %c",str[i]);
            return 0;
            break;
        }
    
        
}
}
int main(){
    char str[100];
    printf("Enter the string\n");
    gets(str);
    // puts(str);
    non_repeating_char(str);
    return 0;
}