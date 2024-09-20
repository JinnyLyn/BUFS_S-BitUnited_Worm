#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

//인풋값 유효여부 확인(아직 안쓰임). 문제있으면 -1 돌려줌.
int validateInput(int min, int max) {
  char input[7];
  int value;

  printf("Please type your selection (%d - %d)\n", min, max);
  if(fgets(input, sizeof(input), stdin) != NULL) {
    input[strcspn(input, "\n")] = 0;

    char *endptr;
    value = strtol(input, &endptr, 10);

    if(*endptr != '\0' || endptr == input || value < min || value > max) {
      printf("Error!!! Invalid input.\nPlease enter a number between %d and %d!\nExiting ...\n", min, max);
      return -1;
    }
    return value;
  }else {
    printf("Error reading input.\nExiting ...\n");
    return -1;
  }
}


//인풋버퍼 초기화
void clrInputBuffer() {
  int c;
  while ((c = getchar()) != '\n' && c != EOF);
}

//encrypt function. 암호화 기능 함수. 숫자로 입력받은  방법으로 switch문에서 각각 암호화 코드 작성
//함수는 암호화된 값을 돌려줘야함.
int encrypting(int method) {
  switch (method) {
    case 1:
    //여따해
  }
}

//decryt function. 복호화 기능 함수. 숫자로 입력받은 방법으로 switch문에서 각각 코드 작성.
//함수는 복호화된 값을 돌려줘야함.
int decrypting(int method) {
  switch (method) {
    case 1:
    //여따해
  }
}

//main. 메인
int main(void) {
  int decrypt_or_encrypt = 0;
  int decrypt_method = 0;
  int encrypt_method = 0;

  printf("Please Select what You want to do: \n");
  printf("[1] Encrypt\n[2]Decrypt\n");
  
  decrypt_or_encrypt = validateInput(1, 2);
  if(decrypt_or_encrypt != -1) {
    clrInputBuffer();

    switch (decrypt_or_encrypt) {
      case 1: //암호화
        printf("Select encrypting method: \n");
        //암호화 방법 몇가지(baseu64 url 등등) 사용해보기.
        printf("[1]asdf\n[2]asdf\n[3]asdf\n[4]asdf\n[5]asdf\n");
        encrypt_method = validateInput(1, 5); //함수 입력값은 선택지에 따라 바뀜
        if(encrypt_method != -1) {
          encrypting(encrypt_method);
          //계속해
        }
      break;

      case 2: //복호화
        printf("Select decrypting method: \n");
        //복호화 방법 몇가지 사용해보기.
        printf("[1]asdf\n[2]asdf\n[3]asdf\n[4]asdf\n[5]asdf\n");
        decrypt_method = validateInput(1, 5); //함수 입력값은 선택지에 따라 바뀜
        if(decrypt_method != -1) {
          decrypting(decrypt_method);
          //계속해
        }
      break;
    }
}
