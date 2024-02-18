#include <stdio.h>
#include <stdlib.h>

int main(){
    int a = 10;
    int *p = &a;
    printf("address of p is %d\n", p); // this is an integer pointer, integer is stored in 4 bits
    printf("Size of integer is %d bytes\n", sizeof(int));
    printf("address of p + 1 is %d\n", p + 1); // this will be the location of the next integer, so p + 1 is actually 4 higher
    printf("value of of p + 1 is %i\n", *(p + 1)); // junk value, nothing saved there
    return 0;
}