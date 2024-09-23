#include <stdio.h>

int main() {
    int data[7] = {6,3,9,7,2,4,1};
    for (int j = 0; j < 6; j++) {
        for (int i = 0; i < 6; i++) {
            int tmp = 0;
            if (data[i] > data[i+1]) {
                tmp = data[i];
                data[i] = data[i+1];
            data[i+1] = tmp;
        } else {

        }
    }
    printf("%d, %d, %d, %d, %d, %d, %d\n", data[0], data[1], data[2], data[3], data[4], data[5], data[6]);

    return 0;
}