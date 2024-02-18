#include <stdio.h>
#include <stdlib.h>

int main(){
    double gpa = 3.5; // I can access the information using variable name
    char grade = 'A'; // C accesses information using memory addresses
    // we use a the pointer for age to access the memory address
    int age = 30; // variable is stored in a specific memory location on ram
    int *p_age = &age; // p_age is a pointer variable which stores the memory address of age
    // I initialize the pointer with the object's data type
    printf("%d\n", *p_age); // de-referencing the pointer to get the value
    printf("%p\n", &age); // %p is the format specifier for memory address
    return 0;
}