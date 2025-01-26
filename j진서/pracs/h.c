#include <stdio.h>

int main(int argc, char *argv[]) {
  if (argc < 2) {
    printf("Please type your First name!\n");
    return 0;
  } else {
    printf("Hello %s!\n", argv[1]);
    return 0;
  }
}
