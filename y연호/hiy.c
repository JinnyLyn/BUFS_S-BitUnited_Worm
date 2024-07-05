#include <stdio.h>
#include <stdlib.h>

void clrInputBuffer() {
    int c;
    while((c = getchar()) != '\n' && c != EOF);
}

void giveBiggerOneBack(void* a, void* b, void* r) {
    if(sizeof(*a) != sizeof(*b)) {
        printf("Two inputs have different size! ABORTING...");
    }
    //under construction. Needs to define the stored data type
    //and cast the void* into what is right.
    else if(*a > *b) {
        *r = *a;
    }else if (*a<*b) {
        *r=*b;
    }else printf("They're the same!");
}

int main() {
    clrInputBuffer();
    int a = 1;
    int b = 4;
    int r = 0;
    giveBiggerOneBack(&a, &b, &r);

}