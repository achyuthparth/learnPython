#include <stdio.h>

// there are 4 parts to how the memory is used: code is stored in the first part [text]
// global variables are stored in the second part [static]
// local variables are stored in the stack, current function stack is paused when another method is called
// this is where the stack is cleared and new local variables are created
// there is also a heap, which is only used during execution
void increment(int *p) {*p ++;}

int main(){
    int x = 5; // variables within a method are local, so when we pass arguments to other functions we use pointers
    int * p = &x;
    int ** q = &p; // we use int** to get a pointer of a pointer of an integer
    int *** r = &q;
    printf("x is currently %d\n", x);
    increment(&x); // the pointer of x is stored separate from the main method's function stack
    printf("x is currently %d\n", x); // this is called called by reference
    return 0;
}