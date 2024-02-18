#include <stdio.h>
#include <stdlib.h>

int main(){
    char character_name[] = "John";
    int character_age = 35;
    printf("There was a man named %s.\n", character_name);
    printf("He was %i years old.\n", character_age);
    character_age = 34;
    printf("He did not like being %d years old.\n", character_age); 
    //%d is different from %i. %d assumes base 10, %i auto-detects base
    return 0;
}