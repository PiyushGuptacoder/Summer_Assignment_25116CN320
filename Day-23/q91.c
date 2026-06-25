#include <stdio.h>
#include <string.h>
int check_anagram(char str1[],char str2[]){
    int n1=strlen(str1);
    int n2=strlen(str2);
    if(n1!=n2){
        printf("The strings are not anagrams\n");
        return 0;
    }
    int count1[256]={0};
    int count2[256]={0};
    for(int i=0;i<n1;i++){
        count1[str1[i]]++;
        count2[str2[i]]++;
    }
    for(int i=0;i<256;i++){
        if(count1[i]==count2[i]){
            continue;
        }
        else{
            printf("The strings are not anagrams\n");
            return 0;
        }
    }
    printf("The strings are anagrams\n");
    return 1;
}
int main(){
    char str1[100],str2[100];
    printf("Enter the string1\n");
    gets(str1);
    printf("Enter the string2\n");
    gets(str2);
    check_anagram(str1,str2);
    return 0;
}