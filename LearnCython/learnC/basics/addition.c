#include <stdio.h>
#include <stdlib.h>

int main(){
    double num1;
    double num2; // using int would result in the answer floored
    printf("Enter first number: \n");
    scanf("%lf", &num1);
    printf("Enter second number: \n");
    scanf("%lf", &num2);
    printf("Answer is %f\n", num1 + num2);
    return 0;
}