#include <stdio.h>
#include <stdlib.h>

int max2(int num1, int num2);
int max3(int num1, int num2, int num3);

int main(){
    printf("%d\n", max2(40, 10));
    printf("%d\n", max3(0, 10, 4));
    if (3 > 2 || 2 < 5){ // or operator is done by ||, this is the non-exclusive or
        printf("True");
    } else{printf("False");}
    if (!(3 > 2 || 2 < 5)){ // using the ! before will negate the predicate
        printf("False");
    } else{printf("True");}
    return 0;
}

int max2(int num1, int num2){
    int result;
    if (num1 > num2){
        return num1;
    } else {return num2;}
}

int max3(int num1, int num2, int num3){
    if (num1 >= num2 && num1 >= num3){ //and operator is done by &&
        return num1;
    } else if (num2 >= num1 && num2 >= num3){ //you can compound else and if for else if for less nesting
        return num2;
    }
    return num3;
}