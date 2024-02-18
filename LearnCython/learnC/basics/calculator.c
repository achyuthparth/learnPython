#include <stdio.h>
#include <stdlib.h>

double add(double num1, double num2) {return num1 + num2;}
double subtract(double num1, double num2) {return num1 - num2;}
double multiply(double factor1, double factor2) {return factor1 * factor2;}
double divide(double divisor, double dividend) {return divisor / dividend;}

int main(){
    double num1;
    double num2;
    char operator;
    double result;
    printf("Enter the first number: \n");
    scanf("%lf", &num1);
    printf("Enter the operator: \n");
    scanf(" %c", &operator); // need to put a space bar before %c when using scanf
    printf("Enter the second number: \n");
    scanf("%lf", &num2);
    if (operator == '+'){result = add(num1, num2);}
    else if (operator == '-') {result = subtract(num1, num2);}
    else if (operator == '*') {result = multiply(num1, num2);}
    else if (operator == '/') {result = divide(num1, num2);}
    else{printf("Invalid Operator");}
    printf("%f %c %f = %f",num1, operator, num2, result);
    return 0;
}