#include <stdio.h>

int main() {
    char data[12] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    data[5] = 1;
    data[11] = 2;
    printf("1 Dimensional array: data[%d] = %d, data[%d] = %d\n", 5, data[5], 11, data[11]);

    char data2[3][4] = {{0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
    data2[1][2] = 1;
    data2[2][3] = 2;
    printf("2 Dimensional array: data[1][2] = %d, data[2][3] = %d\n", data2[1][2], data2[2][3]);
    return 0;
}