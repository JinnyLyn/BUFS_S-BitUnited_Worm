#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#define MAX_ALLOC_VAR 10
void * allocated[MAX_ALLOC_VAR];
int allocated_count = 0;
char mykey[14] = "aSexHagoSipDa";

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
    //todo: 노사장님 크레딧 추가 하기. printf("한남대 ")
    printf("\n\n");
}

void freeMalloc() {
  for (int i = 0; i < allocated_count; i++) {
    free(allocated[i]);
  }
}

//*인풋값 유효여부 확인(아직 안쓰임). 문제있으면 -1 돌려줌.
int validateInput(int min, int max) {
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
void char2binary(char c, char* binary) {
  for (int i = 7; i >= 0; --i) {
    binary[7 - i] = (c & (1 << i)) ? '1' : '0';
  }
  binary[8] = '\0';
}

//*string into binary
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

//*인풋버퍼 초기화
void clrInputBuffer() {
  int c;
  while ((c = getchar()) != '\n' && c != EOF);
}

/**
 * Encryption function. 암호화 기능 함수.
 * @param method Parameter for this function will determine the encryption method.
 */
int encrypting(int method, char* toEncrypt, char* result) {
  switch (method) {
    case 1:
      //인풋값과 내 키를 바이너리로 전환
      string2binary(toEncrypt, result);
      string2binary(mykey, intmykey);
      //전환된 바이너리를 strtol함수로 정수형으로 저장장


      printf("Encrypted:\n%s\n", result);
      break;
  }
}
int main(void) {
  int decrypt_or_encrypt = 0;
  int decrypt_method = 0;
  int encrypt_method = 0;
  char * object_string = (char *)malloc(sizeof(char) * 512);
  allocated[allocated_count++] = object_string;
  char * result_data = (char *)malloc(sizeof(char) * 512);
  allocated[allocated_count++] = result_data;
  char * bin_result;
  int * object_string_long = 0;
  int * mykey_long = 0;

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

}