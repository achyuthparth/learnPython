#include <stdio.h>
#include <stdlib.h>

// structs are similar to class but you don't have methods, only attributes
// you work around the lack of methods by using function pointers
struct Student{
    char name[50]; // defining student attributes
    char major[50];
    int age;
    double gpa;
}; // need to use semicolon when defining struct

int main(){
    struct Student student1;
    student1.gpa = 3.4;
    student1.age = 18;
    // string copy function to make it easier to deal with strings instead of using character arrays
    strcpy(student1.name, "Jim");
    strcpy(student1.major, "Mathematics");
    printf("Student 1's gpa = %f\n", student1.gpa);

    struct Student student2;
    student2.gpa = 3.2;
    student2.age = 8;
    // string copy function to make it easier to deal with strings instead of using character arrays
    strcpy( student2.name, "Ken");
    strcpy( student2.major, "Computer Science");
    printf("Student 2's name is: %s", student2.name);
    
    return 0;
}