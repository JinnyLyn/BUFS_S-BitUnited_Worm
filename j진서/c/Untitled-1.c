#include <stdio.h>
#include <string.h>

int main() {
    char b[2];
    int a;
    printf("Your score: ");
    scanf("%d", &a);

    if (a > 100 || a < 0) {
        printf("DO NOT LIE!!!");
        return 0;
    }

    if (a >= 90) strcpy(b, "A");
    else if (a >= 80) strcpy(b, "B");
    else if (a >= 70) strcpy(b, "C");
    else {
        strcpy(b, "F");
        printf("Score: %d\nGrade: %s\nPlease retake the class next semester.", a, b);
        return 0;
    }
    
    printf("Score: %d\nGrade: %s", a, b);
    return 0;

}