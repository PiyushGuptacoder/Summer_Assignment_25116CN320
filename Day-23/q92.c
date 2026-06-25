#include <stdio.h>
#include <string.h>
int find_max_char(char str1[]){
    int n1=strlen(str1); 
    int count1[256]={0};
    // int count2[256]={0};
    for(int i=0;i<n1;i++){
        count1[str1[i]]++;
    }
    int c=0,i,maxchar;
    for(i=0;i<256;i++){
        if(count1[i]>c){
            c=count1[i];
            maxchar=(char)i;
        }
        
    }
    printf("The maximum occurring character is '%c' and it occurs %d times\n",maxchar,c);
    return 1;
}
int main(){
    char str1[100];
    printf("Enter the string1\n");
    gets(str1);
    find_max_char(str1);
    return 0;
}