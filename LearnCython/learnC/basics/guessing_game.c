#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> // adding this so we can use boolean variables

int main(){
    int secret = 5;
    int guess;
    int guess_count = 0;
    bool out_of_guesses = false;
    while (guess != secret && out_of_guesses == false){
        if (guess_count < 3){
            printf("Guess the number, you have %d tries left: \n", 3 - guess_count);
            scanf("%d", &guess);
            guess_count ++;
            if (guess == secret) {break;}
        } else {
            out_of_guesses = true;
            printf("Out of guesses :(");
            }
    }
    if (out_of_guesses == false) {printf("Correct!");}
    return 0;
}