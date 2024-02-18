#include <stdio.h>
#include <stdlib.h>

// functions need to be defined prior, else the main method will not be able to call it
// we solve this by prototyping

double cube(double factor);
double cube2(double factor);
void greetings(char name[]);

int main(){
    greetings("Mike Tyson"); // function won't execute unless you call it
    greetings("Conor McGregor");
    printf("2 ^ 3 = %f\n3 ^ 3 = %f ", cube(2), cube2(3));
    return 0;
}

double cube(double factor){
    double result = factor * factor * factor;
    return result;
}

double cube2(double factor){
    return factor * factor * factor;
}

// void means no return statement
void greetings(char name[]){
    printf("Hello %s\n", name);
}
