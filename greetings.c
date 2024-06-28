#include <stdio.h>

void clrInputBuffer() {
  char c;
  while(c = getchar() != '\0' && EOF);
}


void getName(char *name, int check) {
  if (check != 1) {
    printf("E -1\n");
    return -1;
  }

  char name = (char*)malloc(sizeof(char) * );
  while(1) {
    clrInputBuffer();
    printf("Your name: ");
    
  }

  return *name;
}

int main() {

}