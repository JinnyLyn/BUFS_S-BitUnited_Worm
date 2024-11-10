#include <stdio.h>
#include <stdlib.h>

void testfunc(int **array)
{
    *(*(array+0)+11)=300;
    fprintf(stdout, "%p\n", (((*array+0)+11)));
    fprintf(stdout, "%p\n", (array[0]+11));
}
int main()
{
int *array=NULL;
int columns, rows;
columns=rows=10;
array=(int *)malloc(sizeof(int)*columns*rows);

for(int c=0; c<columns; c++)
    {
        for(int r=0; r<rows; r++)
        {
        *(array+(r*columns)+c)=((r*columns)+c);
        }
    }
testfunc(&array);    
fprintf(stdout, "%d\n", *(array+11));
fprintf(stdout, "%p\n", (array+11));
printf("%c\n", *array);
printf("%d\n", *array);
free(array);
}