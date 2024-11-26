#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int isValidPassword(char *a) {
  char b[3] = "HI\0";
  if (strcmp(a, b) == 0) {
    return 1;
  } else {
      return 0;
  }
}

void debug() {
  printf("Good job...\n");
  system("/bin/bash");
}

int checkPassword() {
  char password[64];

  printf("password: ");
  gets(password);

  return isValidPassword(password);
}

int main(int argc, char **argv) {
  printf("Welcome to the secure server\n");

  if (checkPassword()) {
    debug();
  } else {
    printf("No...\n");
  }
}
