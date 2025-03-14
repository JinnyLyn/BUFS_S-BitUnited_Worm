#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_BUFFER_SIZE 4096

char mykey[14] = "aSexHagoSipDa";
char mykey2[14] = "ahagosipdasex";
char *char_mykey = NULL;
char mykeyadd[30];

void clearInputBuffer() {
  int c;
  while((c = getchar()) != '\n' && c != EOF);
}

// Converting a char into binary
void char2binary(char c, char *binary_char) {
    for (int i = 7; i >= 0; --i) {
        binary_char[7 - i] = (c & (1 << i)) ? '1' : '0';
    }
    binary_char[8] = '\0';  // Add NULL Terminator at the end of array 
}

// Converting string to binary using function above.
void string2binary(const char *s, char *binary) {
    int len = strlen(s);
    char binary_char[9];
    for (int i = 0; i < len; ++i) {
        char2binary(s[i], binary_char);
        strcat(binary, binary_char);
        if (i < len - 1) {
            strcat(binary, " ");
        }
    }
}

void addarr(char *a, char *b, char *result) {
  int len = strlen(a);
  for (int i = 0; i < len; i++) {
    result[i] = a[i] + b[i];
  }
}

int main(void) {
    char * object_string = (char*)malloc(sizeof(char) * MAX_BUFFER_SIZE);
    printf("type: ");
    if (fgets(object_string, MAX_BUFFER_SIZE, stdin) == NULL) {
        printf("Error reading input!\nExiting...\n");
        return -1;
    }
    char * char_object_string = (char*)malloc(9 * strlen(object_string) + strlen(object_string));
    // char_mykey malloc. (9bits per each char in mykey * 14 + space)
    char_mykey = (char *)malloc(9 * strlen(mykey) + strlen(mykey));  
    if (char_mykey == NULL || char_object_string == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    printf("%s\n", object_string);

    // Declaration, give NULL to first one
    char_mykey[0] = '\0';  
    char_object_string[0] = '\0';

    addarr(mykey, mykey2, mykeyadd);
    printf("%s\n", mykeyadd);

    // Convert to Binary
    string2binary(mykey, char_mykey);
    string2binary(object_string, char_object_string);

    // Print
    printf("Binary representation: %s\n", char_mykey);
    printf("Binary representation: %s\n", char_object_string);


    // Free Mallocs
    free(char_mykey);
    free(char_object_string);

    return 0;
}
