#include <stdio.h>
#include <string.h>
int isPalindrome(char str[]) {
    int start = 0;
    int len = strlen(str);

    while (start < len-1) {
        if (str[start] != str[len-1]) {
            return 0;
        }
        start++;
        len--;
    }
    return 1;
}
int main() {
    char str[100];
    printf("Enter a string: ");
    scanf("%s", str);
if (isPalindrome(str)) {
        printf("Palindrome string\n");
    } 
else {
        printf("Not a palindrome string\n");
    }

    return 0;
}