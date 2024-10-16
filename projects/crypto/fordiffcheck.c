#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_ALLOC_VAR 10

void *allocated[MAX_ALLOC_VAR];
int allocated_count = 0;
char mykey[14] = "aSexHagoSipDa";
char *char_object_string = NULL;
char *char_mykey = NULL;
int *int_mykey = NULL;
int *int_object_string = NULL;
int *addmykeyobjectstring = NULL;
int *xormykeyobjectstring = NULL;

/*
 * Return codes:
 *  0: successfully finished task
 * -1: error reading input
 * -2: memory allocation failure
 * -3: encryption failure
 */
char err1[39] = "Error Reading Input!!!\nExiting ...\n";
char err2[54] = "Memory allocation Failure!!!\nExiting ...\n";
char err3[37] = "Encryption Failure!!!\nExiting ...\n";
// Initial message
void InitialMessage() {
    printf("_________ .__       .__                                           __               __            __________              ____.__        \n");
    printf("\\_   ___ \\|__|_____ |  |__   ___________  _____________  ____    |__| ____   _____/  |_          \\______   \\___.__.     |    |__| ____  \n");
    printf("/    \\  \\/|  \\____ \\|  |  \\_/ __ \\_  __ \\ \\____ \\_  __ \\/  _ \\   |  |/ __ \\_/ ___\\   __\\          |    |  _<   |  |     |    |  |/    \\ \n");
    printf("\\     \\___|  |  |_> >   Y  \\  ___/|  | \\/ |  |_> >  | \\(  <_> )  |  \\  ___/\\  \\___|  |            |    |   \\\\___  | /\\__|    |  |   |  \\\n");
    printf(" \\______  /__|   __/|___|  /\\___  >__|    |   __/|__|   \\____/\\__|  |\\___  >\\___  >__|    ______  |______  // ____| \\________|__|___|  /\n");
    printf("        \\/   |__|        \\/     \\/        |__|               \\______|    \\/     \\/       /_____/         \\/ \\/                       \\/ \n");
    // todo: 노사장님 크레딧 추가 하기. printf("한남대 ")
    printf("\n\n");
}

void freeMalloc() {
    for (int i = 0; i < allocated_count; i++) {
        free(allocated[i]);
    }
}

// Input validation
int validateInput(int min, int max) {
    char input[sizeof(int)];
    int value;

    printf("Please type your selection (%d - %d)\n", min, max);
    if (fgets(input, sizeof(input), stdin) != NULL) {
        input[strcspn(input, "\n")] = 0;

        char *endptr;
        value = strtol(input, &endptr, 10);

        if (*endptr != '\0' || endptr == input || value < min || value > max) {
            fprintf(stderr, "Error!!! Invalid input.\nPlease enter a number between %d and %d!\nExiting ...\n", min, max);
            return -1;
        }
        return value;
    } else {
        fprintf(stderr, "%s\n", err1);
        return -1;
    }
}

// Convert char to binary
void char2binary(char c, char *binary) {
    for (int i = 7; i >= 0; --i) {
        binary[7 - i] = (c & (1 << i)) ? '1' : '0';
    }
    binary[8] = '\0';
}

// Convert string to binary
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

// Clear input buffer
void clrInputBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

// Encryption function
int encrypting(int method, char *object_string) {
    switch (method) {
        case 1:
            // Convert input and key to binary
            int input_len = strlen(object_string);
            int key_len = strlen(mykey);
            int bin_len = input_len * 9; // Each char converts to 8 bits + 1 space
            int key_bin_len = key_len * 9;

            char_object_string = (char *)malloc(bin_len + 1);
            char_mykey = (char *)malloc(key_bin_len + 1);

            if (char_object_string == NULL || char_mykey == NULL) {
                fprintf(stderr, "%s\n", err2);
                freeMalloc();
                return -2;
            }

            allocated[allocated_count++] = char_object_string;
            allocated[allocated_count++] = char_mykey;

            string2binary(object_string, char_object_string);
            string2binary(mykey, char_mykey);

            // Convert binary strings to integers
            int_mykey = (int *)malloc(sizeof(int));
            int_object_string = (int *)malloc(sizeof(int));

            if (int_mykey == NULL || int_object_string == NULL) {
                fprintf(stderr, "%s\n", err2);
                freeMalloc();
                return -2;
            }

            allocated[allocated_count++] = int_mykey;
            allocated[allocated_count++] = int_object_string;

            *int_mykey = strtol(char_mykey, NULL, 2);
            *int_object_string = strtol(char_object_string, NULL, 2);
            strtol(char_mykey, &int_mykey, 2);

            // Add mykey to object_string
            addmykeyobjectstring = (int *)malloc(sizeof(int));
            allocated[allocated_count++] = addmykeyobjectstring;
            *addmykeyobjectstring = *int_object_string + *int_mykey;

            // XOR mykey with object_string
            xormykeyobjectstring = (int *)malloc(sizeof(int));
            allocated[allocated_count++] = xormykeyobjectstring;
            *xormykeyobjectstring = *int_object_string ^ *int_mykey;

            printf("Encrypted value (XOR): %d\n", *xormykeyobjectstring);
            break;
    }
    return 0;
}

int main(void) {
    int decrypt_or_encrypt = 0;
    int encrypt_method = 0;
    char *object_string = (char *)malloc(sizeof(char) * 512);
    allocated[allocated_count++] = object_string;
    char *result_data = (char *)malloc(sizeof(char) * 512);
    allocated[allocated_count++] = result_data;

    if (object_string == NULL || result_data == NULL) {
        fprintf(stderr, "%s", err2);
        freeMalloc();
        return -2;
    }

    // Print out initial message
    InitialMessage();

    printf("This is a basic decrypt/encrypt program.\n");
    printf("What has been encrypted using this program is only decrypt-able with this one. (Ideally...)\n");
    printf("This program only works with English Alphabets on current version!");
    printf("Enter what you want to decrypt/encrypt: \n");
    if (fgets(object_string, sizeof(object_string), stdin) != NULL) {
        object_string[strcspn(object_string, "\n")] = '\0';
    } else {
        printf("Error reading input.\nExiting...\n");
        freeMalloc();
        return -1;
    }

    printf("Please Select what You want to do: \n");
    printf("[1]Encrypt\n[2]Decrypt\n");

    decrypt_or_encrypt = validateInput(1, 2);
    if (decrypt_or_encrypt != -1) {
        clrInputBuffer();

        switch (decrypt_or_encrypt) {
            case 1: // Encrypt
                printf("Select encrypting method(#1 will be based on my own algorithm.): \n");
                printf("[1]CIPHER\n[2]asdf\n[3]asdf\n[4]asdf\n[5]asdf\n");
                encrypt_method = validateInput(1, 5); // Function input value changes based on selection
                if (encrypt_method != -1) {
                    encrypting(encrypt_method, object_string);
                }
                break;

            /*case 2: // Decrypt
                printf("Select decrypting method(use #1 if you used this program to encrypt.): \n");
                printf("[1]DCIPHER\n[2]asdf\n[3]asdf\n[4]asdf\n[5]asdf\n");
                decrypt_method = validateInput(1, 5); // Function input value changes based on selection
                if (decrypt_method != -1) {
                    decrypting(decrypt_method, object_string);
                }
                break;*/
        }
    } else {
        printf("Invalid input. Exiting...\n");
        freeMalloc();
        return -1;
    }

    freeMalloc();
    return 0;
}
