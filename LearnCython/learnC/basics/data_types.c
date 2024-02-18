#include <stdio.h>
#include <stdlib.h>

int main(){
    int age = 40;
    double gpa = 3.7; //double has 15 decimal digits, float has 7 decimal digits
    char grade = 'A'; //single quotation marks for singular characters
    char phrase[] = "Hello"; //use double quotation marks for a string -> this is an array of characters
    printf("example \"quotes\"\n");
    printf("There is a number %d\n", 500);
    printf("The phrase is %s, and the age is %d\n", phrase, age);
    printf("The gpa is %f which is an %c\n", gpa, grade);
    //format specifier such as %d [integers] %s [strings] %f [decimal number] %c [single character]
    return 0;
}