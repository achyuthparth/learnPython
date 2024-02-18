#include <stdio.h>
#include <stdlib.h>

int main(){
    char grade = 'A';
    switch (grade){ // we can use case instead of a bunch of if else statements
    case 'A':
        printf("You did well!");
        break; // break allows us to leave the switch statements
    case 'B':
        printf("You did alright.");
        break;
    case 'C':
        printf("You did mediocre");
        break;
    case 'D':
        printf("You did not do well.");
        break;
    case 'F':
        printf("You did horribly!");
        break;
    
    default: // in case there is not a single working case
        printf("Invalid Grade");
        break;
    }
    return 0;
}