#include <stdio.h>
#include <string.h>

    int main() {
    int score;
    char grade[2];
    
    printf("Your score: ");
    scanf("%d", &score);

    switch (score / 10) {
        case 10:
        case 9:
            strcpy(grade, "A");
            break;
        case 8:
            strcpy(grade, "B");
            break;
        case 7:
            strcpy(grade, "C");
            break;
        default:
            strcpy(grade, "F");
            printf("Your Grade is %s!\nPlease retake the class next semester!!", grade);
            return 0;
    }
    printf("Your score: %d\nYour Grade: %s\n", score, grade);
    return 0;
}
