#include <stdio.h>
#include <stdlib.h>

int main(){
    char name2[20];
    printf("Enter your full name: \n");
    fgets(name2, 20, stdin); //stdin stands for standard input, 20 is the string length limit, this will scan spaces
    // fgets will also add a \n at the end of the input
    printf("Your name is %s\n", name2);

    char grade;
    printf("Enter your grade: \n");
    scanf("%c", &grade); // the & is for a pointer
    printf("Your grade is %c\n", grade);

    char name[20]; // need to specify beforehand how many slots needed for the array of characters
    printf("Enter your name: \n");
    scanf("%s", &name); // this will only scan characters until a space occurs
    printf("Your name is %s\n", name);

    int age;
    printf("Enter your age: \n");
    scanf("%d", &age);
    printf("You are %d years old\n", age);

    double gpa;
    printf("Enter your GPA: \n");
    scanf("%lf", &gpa); // need to use lf for scanf function
    printf("Your GPA is %f\n", gpa);

    return 0;
}

// char grade would not run at the bottom
// char name[20] would not run at the bottom
// char name2[20] would only run at the top