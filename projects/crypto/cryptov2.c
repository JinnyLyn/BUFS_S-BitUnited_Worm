#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define MAX_ALLOC_VAR 10
#define MAX_BUFFER_SIZE 4096
#define MAX_BINARY_SIZE 32768

void * allocated[MAX_ALLOC_VAR];
int allocated_count = 0;
char mykey[14] = "aSexHagoSipDa";
char* char_object_string = 0;
char* char_mykey = 0;
int * int_mykey = 0;
int * int_object_string = 0;
int * addmykeyobjectstring = 0;
int * xormykeyobjectstring = 0;

/*
 * *return codes:
 * * 0: successfully finished task
 * *-1: error reading input
 * *-2: memory allocation failure
 * *-3: encryption failure
 */
char err1[39] = "Error Reading Input!!!\nExiting ...\n";
char err2[54] = "Memory allocation Failure!!!\nExiting ...\n";
char err3[37] = "Encryption Failure!!!\nExiting ...\n";

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

//*인풋값 유효여부 확인(아직 안쓰임). 문제있으면 -1 돌려줌.
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

//*char to binary
void char2binary(char c, char * binary) {
  for (int i = 7; i >= 0; --i) {
    binary[7 - i] = (c & (1 << i)) ? '1' : '0';
  }
  binary[8] = '\0';
}

//*string into binary
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

//*인풋버퍼 초기화
void clrInputBuffer() {
  int c;
  while ((c = getchar()) != '\n' && c != EOF);
}

/**
 * Encryption function. 암호화 기능 함수.
 * @param method Parameter for this function will determine the encryption method.
 */
int encrypting(int method, char* object_string) {
  switch (method) {
    case 1:
      //인풋값과 내 키를 바이너리로 전환
      string2binary(object_string, char_object_string);
      string2binary(mykey, char_mykey);
      //전환된 바이너리를 strtol함수로 정수형으로 저장
      *int_mykey = strtol(char_mykey, &char_mykey, 10);
      *int_object_string = strtol(char_object_string, &char_object_string, 10);
      //add mykey to object_string
      //todo: MUST ALLOCATE ENOUGH MEMORY
      addmykeyobjectstring = (int *)malloc(sizeof(int));
      allocated[allocated_count++] = addmykeyobjectstring;
      *addmykeyobjectstring = *int_object_string + *int_mykey;
      //xor mykey with object_string
      //todo: MUST ALLOCATE ENOUGH MEMORY
      xormykeyobjectstring = (int *)malloc(sizeof(int));
      allocated[allocated_count++] = xormykeyobjectstring;
      *xormykeyobjectstring = *int_object_string ^ *int_mykey;

     // printf("%d\n", *xormykeyobjectstring);
      break;
  }
}

/**
 * Decryption function. 복호화 기능 함수.
 * @param method Parameter for this function will determine the decryption method.
 */
/*int decrypting(int method, char* toEncrypt, char* result) {
  switch (method) {
    case 1:
    //여따해
  }
}*/

//main
int main(void) {
  int decrypt_or_encrypt = 0;
  int decrypt_method_selection = 0;
  int encrypt_method_selection = 0;
  char * object_string = (char *)malloc(sizeof(char) * MAX_BUFFER_SIZE);
  allocated[allocated_count++] = object_string;
  char * result_data = (char *)malloc(sizeof(char) * MAX_BINARY_SIZE);
  allocated[allocated_count++] = result_data;
  char * bin_result;

  if (object_string == NULL || result_data == NULL) {
    fprintf(stderr, "%s", err2);
  
    freeMalloc();
    return -2;
  }
  //print out initial message
  InitialMessage();

  

  printf("This is a basic decrypt/encrypt program.\n");
  printf("What has been encrypted using this program is only decrypt-able with this one. (Ideally...)\n");
  printf("This program only works with English Alphabets on current version!");
  printf("Enter what you want to decrypt/encrypt: \n");
  if (fgets(object_string, sizeof(object_string), stdin)!= NULL) {
    object_string[strcspn(object_string, "\n")] = '\0';
  } else {
    printf("Error reading input.\nExiting...\n");
    freeMalloc();
    return -1;
  }

    //calculating memories needed and allocating them for binary converting function.
  /*int input_len = strlen(object_string);
  int bin_len = input_len * 9;
  bin_result = (char*)malloc(sizeof(char) * bin_len);1
  allocated[allocated_count++] = bin_result;
  if (bin_result == NULL) {
    fprintf(stderr, "%s\n", err2);
	free(bin_result);
	freeMalloc();
    return -2;
  }*/

  printf("Please Select what You want to do: \n");
  printf("[1]Encrypt\n[2]Decrypt\n");
  
  decrypt_or_encrypt = validate_selection(1, 2);
  if(decrypt_or_encrypt != -1) {
    clrInputBuffer();

    switch (decrypt_or_encrypt) {
      case 1: //암호화
        printf("Select encrypting method(#1 will be based on my own algorithm.): \n");
        //암호화 방법 몇가지(base64 url 등등) 사용해보기.
        printf("[1]CIPHER\n[2]asdf\n[3]asdf\n[4]asdf\n[5]asdf\n");
        encrypt_method_selection = validate_selection(1, 5); //함수 입력값은 선택지에 따라 바뀜
        if(encrypt_method_selection != -1) {
          encrypting(encrypt_method_selection, object_string);
          //계속해
        }
      break;

      /*case 2: //복호화
        printf("Select decrypting method(use #1 if you used this program to encrypt.): \n");
        //복호화 방법 몇가지 사용해보기.
        printf("[1]DCIPHER\n[2]asdf\n[3]asdf\n[4]asdf\n[5]asdf\n");
        decrypt_method_selection = validate_selection(1, 5); //함수 입력값은 선택지에 따라 바뀜
        if(decrypt_method_selection != -1) {
          decrypting(decrypt_method_selection, object_string);
          //계속해
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