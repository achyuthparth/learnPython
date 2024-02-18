#include <stdio.h>
#include <stdlib.h>

int main(){
    int a; // create integer
    int *p; // create pointer variable for integer
    a = 10; // set integer value
    printf("a is %d\n", a);
    p = &a; // set pointer value
    printf("a is stored at %i\n", p);
    *p = 13; // change value of pointer's reference
    printf("a is now %d\n", *p); // initial integer value is also changed
    int b = 20;
    *p = b; // this will change the value of a to what b is [20]
    printf("*p is now %d\n", *p); // initial integer value is also changed
    printf("b is %d\n", b);
    printf("b is located %d\n", &b);
    printf("a is located %d\n", &a);
    printf("p is located %d\n", &p);
    return 0;
}