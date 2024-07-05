#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <string.h>

/*This shit is created by GPT-4o for experimental purpose. I didn't write it.*/
void clrInputBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

void getInput(char *buffer, size_t size) {
    if (fgets(buffer, size, stdin) != NULL) {
        size_t len = strlen(buffer);
        if (len > 0 && buffer[len - 1] == '\n') {
            buffer[len - 1] = '\0';
        } else {
            clrInputBuffer();
        }
    } else {
        buffer[0] = '\0';
    }
}

// Function to evaluate the expression
double evaluateExpression(const char *expression);

// Helper functions for evaluating the expression
int precedence(char op);
double applyOp(double a, double b, char op);
double parseNumber(const char **expression);

int main() {
    char input[100];
    printf("This is a simple calculator.\n");

    while (1) {
        printf("Enter the expression you want to calculate: ");
        getInput(input, sizeof(input));

        if (input[0] == '\0') {
            printf("Input Handling Error! Please type in a valid expression.\n");
            continue;
        }

        double result = evaluateExpression(input);
        printf("Result: %lf\n", result);
    }

    return 0;
}

int precedence(char op) {
    switch (op) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        case '^':
            return 3;
        default:
            return 0;
    }
}

double applyOp(double a, double b, char op) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return a / b;
        case '^': return pow(a, b);
        default: return 0;
    }
}

double parseNumber(const char **expression) {
    double result = 0;
    while (isdigit(**expression) || **expression == '.') {
        if (**expression == '.') {
            (*expression)++;
            double factor = 0.1;
            while (isdigit(**expression)) {
                result += (**expression - '0') * factor;
                factor *= 0.1;
                (*expression)++;
            }
            break;
        } else {
            result = result * 10 + (**expression - '0');
            (*expression)++;
        }
    }
    return result;
}

double evaluateExpression(const char *expression) {
    double values[100];
    char ops[100];
    int valIndex = 0, opsIndex = 0;

    while (*expression) {
        if (isspace(*expression)) {
            expression++;
            continue;
        }

        if (isdigit(*expression)) {
            values[valIndex++] = parseNumber(&expression);
        } else if (*expression == '(') {
            ops[opsIndex++] = *expression;
            expression++;
        } else if (*expression == ')') {
            while (opsIndex > 0 && ops[opsIndex - 1] != '(') {
                double b = values[--valIndex];
                double a = values[--valIndex];
                char op = ops[--opsIndex];
                values[valIndex++] = applyOp(a, b, op);
            }
            opsIndex--; // Pop '('
            expression++;
        } else if (strchr("+-*/^", *expression)) {
            while (opsIndex > 0 && precedence(ops[opsIndex - 1]) >= precedence(*expression)) {
                double b = values[--valIndex];
                double a = values[--valIndex];
                char op = ops[--opsIndex];
                values[valIndex++] = applyOp(a, b, op);
            }
            ops[opsIndex++] = *expression;
            expression++;
        } else {
            printf("Invalid character in expression: %c\n", *expression);
            return 0;
        }
    }

    while (opsIndex > 0) {
        double b = values[--valIndex];
        double a = values[--valIndex];
        char op = ops[--opsIndex];
        values[valIndex++] = applyOp(a, b, op);
    }

    return values[0];
}
