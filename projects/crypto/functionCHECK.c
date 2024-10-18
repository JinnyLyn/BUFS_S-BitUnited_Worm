#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

char mykey[14] = "aSexHagoSipDa";
char *char_mykey = NULL;

// char을 이진수로 변환하는 함수 작성
void char2binary(char c, char *binary_char) {
    for (int i = 7; i >= 0; --i) {
        binary_char[7 - i] = (c & (1 << i)) ? '1' : '0';
    }
    binary_char[8] = '\0';  // 문자열 끝에 NULL 추가
}

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

int main(void) {
    char * object_string = (char*)malloc(1024);
    printf("type: ");
    if (fgets(object_string, sizeof(object_string), stdin) == NULL) {
        printf("Error reading input!\nExiting...\n");
        return -1;
    }
    char * char_object_string = (char*)malloc(9 * strlen(object_string) + strlen(object_string));
    // char_mykey에 메모리 할당 (mykey의 각 문자에 대해 9비트 * 14 + 공백)
    char_mykey = (char *)malloc(9 * strlen(mykey) + strlen(mykey));  
    if (char_mykey == NULL || char_object_string == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    //todo: 여기 시발 왜 오류남?
    //object_string이 마치 8바이트로 고정된거같음. 문자 7개만 읽는데 이유를 모르겠음.
    printf("%s\n", object_string);
    int len = sizeof(char_object_string);
    printf("%d\n", len);
    char_mykey[0] = '\0';  // 초기화를 위해 첫 글자에 NULL 값 설정
    char_object_string[0] = '\0';

    // 이진 변환
    string2binary(mykey, char_mykey);
    string2binary(object_string, char_object_string);

    // 출력
    printf("Binary representation: %s\n", char_mykey);
    printf("Binary representation: %s\n", char_object_string);


    // 메모리 해제
    free(char_mykey);
    free(char_object_string);

    return 0;
}