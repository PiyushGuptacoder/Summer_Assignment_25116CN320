#include <stdio.h>
#include <string.h>

void charFreq(char str[]) {
    int freq[256] = {0};

    for (int i = 0;i<strlen(str); i++) {
        freq[(unsigned char)str[i]]++;
    }

    printf("Character frequencies:\n");
    for (int i = 0; i < 256; i++) {
        if (freq[i] > 0) {
            printf("%c → %d\n", i, freq[i]);
        }
    }
}

int main() {
    char str[100];
    printf("Enter a string: ");
    gets(str);
    str[strcspn(str, "\n")] = '\0';

    charFreq(str);
    return 0;
}
