#include <stdio.h>

int main() {
    int a = 3;
    printf("%d\n", &a);
    void*pa = &a;
    *(int*)pa = 10;
    printf("%d\n", a);
}