#include <stdio.h>

int main() {
    short data1[9] = {4,6,9,8,7,2,5,1,3};

    short tmp = data1[0];
    for (int i = 0; i < 9; i++) {
        if (data1[i] > tmp) {
            tmp = data1[i];
        }
    }
    printf("The biggest number is %d\n", tmp);

    return 0;
}