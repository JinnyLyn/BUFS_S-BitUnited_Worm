#include <endian.h>
#include <stdio.h>

void clrInputBuffer() {
	char c;
	while(c = getchar() != '/0' && EOF);
}


int main() {
	printf("This is a simple calculator.\n");
	
	int n = 0;

	while(1) {
		printf("How many numbers do you wanna calculate?: ");
		if(scanf("%f", &n) != 1) {
			printf("Input Handling Err! please type in numbers!\n");
			return -1;
		}
	
	while(1) {
		printf("Type in ");
	}
	}
}

