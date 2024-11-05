#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX_ALLOC_VAR 10
#define BUFFER_SIZE 4096

void * allocated[MAX_ALLOC_VAR];
int allocated_count = 0;
int allocated_count = 0;
char mykey[] = "mykey";
char object_string[BUFFER_SIZE];
int *addmykeyobjectstring = 0;
int *xormykeyobjectstring = 0;

/*
* return codes:
* 0: execution success
* -1: err reading input
* -2: memory allocation failure
* -3: encryption failure
*/
char err1[39] = "Error Reading Input!!!\nExiting...\n";
char err2[54] = "Memory failure\nExiting...\n";
char err3[37] = "Undefined error\nExiting...\n";

//Initial message
void InitialMessage() {
    printf("_________ .__       .__                                           __               __            __________              ____.__        \n");
    printf("\\_   ___ \\|__|_____ |  |__   ___________  _____________  ____    |__| ____   _____/  |_          \\______   \\___.__.     |    |__| ____  \n");
    printf("/    \\  \\/|  \\____ \\|  |  \\_/ __ \\_  __ \\ \\____ \\_  __ \\/  _ \\   |  |/ __ \\_/ ___\\   __\\          |    |  _<   |  |     |    |  |/    \\ \n");
    printf("\\     \\___|  |  |_> >   Y  \\  ___/|  | \\/ |  |_> >  | \\(  <_> )  |  \\  ___/\\  \\___|  |            |    |   \\\\___  | /\\__|    |  |   |  \\\n");
    printf(" \\______  /__|   __/|___|  /\\___  >__|    |   __/|__|   \\____/\\__|  |\\___  >\\___  >__|    ______  |______  // ____| \\________|__|___|  /\n");
    printf("        \\/   |__|        \\/     \\/        |__|               \\______|    \\/     \\/       /_____/         \\/ \\/                       \\/ \n");
    printf("special thanks to donggeunlee\n");
    printf("\n\n");
}

void freeMalloc() {
    for (int i = 0; i < allocated_count; i++) {
        free(allocated[i]);
    }
}

//this will prompt the user to enter selection and validate it
int validate_selection(int min, int max) {
    char input[sizeof(int)];
    int value;

    printf("Please type your selection (%d - %d)\n", min, max);
    if(fgets(input, sizeof(input), stdin) != NULL) {
    input[strcspn(input, "\n")] = 0;

    char *endptr;
    value = strtol(input, &endptr, 10);

    if(*endptr != '\0' || endptr == input || value < min || value > max) {
        fprintf(stderr, "Error!!! Invalid input.\nPlease enter a number between %d and %d!\nExiting ...\n", min, max);
        return -1;
    }
    return value;
    }else {
    fprintf(stderr, "%s\n", err1);
    return -1;
    }
}

//char to bin
void char2binary(char c, char *binary) {
    for (int i = 7; i >= 0; --i) {
        binary[7 - i] = (c & (1 << i)) ? '1' : '0';
    }
    binary[8] = '\0';
}

//string into binary
void string2binary(const char *s, char* binary) {
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

void clrInputBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c!= EOF);
}

/*
* Encryption function. 암호화 함수.
* @param method Parameter for this function will determine the encryption method.
*/
int encrypt(int method, char *object_string) {
    switch (method) {
        case 1:
            *addmykeyobjectstring = *object_string + *mykey;
            *xormykeyobjectstring = *object_string ^ *mykey;
            
    }
}

/*
* Decryption Function. 복호화 함수.
* @param method Parameter for this function will determine the decryption method.
*/
//int decrypt(int method, char *object_string)

//*main
int main(void) {
    int decrypt_or_encrypt = 0;
    int decrypt_method_selection = 0;
    int encrypt_method_selection = 0;
    //todo: char *result_data = (char *)malloc(sizeof(char) * BIN);

    InitialMessage();
    printf("This is a basic decrypt/encrypt program.\n");
    printf("What has been encrypted using this program is only decrypt-able with this one. (Ideally...)\n");
    printf("This program only works with English Alphabets on current version!");
    printf("Enter what you want to decrypt/encrypt: \n");
    if (fgets(object_string, BUFFER_SIZE, stdin) != NULL) {
        object_string[strcspn(object_string, "\n")] = '\0';
    } else {
        fprintf(stderr, "%s", err1);
        freeMalloc();
        return -1;
    }

    int objs_bin_len = strlen(object_string) * 8 + 1;
    int result_data[objs_bin_len];
    allocated[allocated_count++] = result_data;

    printf("Please Select what You want to do: \n");
    printf("[1]Encrypt\n[2]Decrypt\n");

    decrypt_or_encrypt = validate_selection(1, 2);
    if (decrypt_or_encrypt != -1) clrInputBuffer();

    switch (decrypt_or_encrypt) {
        case 1: // Encrypt
            printf("Select encrypting method(#1 will be based on my own algorithm.): \n");
            //암호화 방법 몇가지(base64 url 등등) 사용해보기.
            printf("[1]CIPHER\n[2]asdf\n[3]asdf\n[4]asdf\n[5]asdf\n");
            encrypt_method_selection = validate_selection(1, 5); //함수 입력값은 선택지에 따라 바뀜
            if(encrypt_method_selection != -1) {
                encrypt(encrypt_method_selection, object_string);
                //continue
            }
            break;
        case 2: // Decrypt
            printf("Select decrypting method(only choose 1 if you encrypted using this program.): \n");
            printf("[1]CIPHER\n[2]asdf\n[3]asdf\n[4]asdf\n[5]asdf\n");
            decrypt_method_selection = validate_selection(1, 5); //함수 입력값은 선택지에 따라 바뀜
            if(decrypt_method_selection != -1) {
                decrypt(decrypt_method_selection, object_string);
            }
        default:
            fprintf(stderr, "%s", err3);
            freeMalloc();
            return -3;
        }

    freeMalloc();
    return 0;
}