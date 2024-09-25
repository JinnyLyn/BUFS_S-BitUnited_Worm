#include <stdio.h>
#include <string.h>

void clrInputBuffer() {
    int c;
    while((c = getchar())!= '\n' && c!= EOF);
}

int main() {
    char input[100];

    printf("Enter a string: ");
    if (fgets(input, sizeof(input), stdin)) {
        input[strcspn(input, "\n")] = '\0'; // Remove newline character
        printf("You entered: %s\n", input);
    } else {
        printf("Error reading input.\n");
    }

    return 0;
}