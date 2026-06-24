#include  <stdio.h>
int len_str(char str[]){
    int i=0;
    while(str[i]!='\0'){
        i++;
    }
    return i;
}
int count_vow_con(char str[]){
    int vow=0,cons=0;
    for (int i=0;i<len_str(str);i++){
        if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u'||str[i]=='A'||str[i]=='E'||str[i]=='I'||str[i]=='O'||str[i]=='U'){
            vow++;
        }
        else{
            cons++;
        }
    }
    printf("The number of vowels is %d and consonants is %d",vow,cons);

}

int main(){
    char str[10];
    printf("Enter the string ");
    scanf("%s",str);
    count_vow_con(str);
    return 0;


}