#include <stdio.h>
#include <stdlib.h>

int main(){
    int index = 1;
    while(index <= 5){ // this will only run if the condition is true
        printf("%d\n", index);
        index ++;
    } // beware of infinite loops, if we did not have index++ it will run forever

    int index2 = 6;
    do { // this will run one iteration regardless of the looping condition
        printf("%d\n", index2);
        index2 ++;
    }while (index2 <= 5);
    
    return 0;
}