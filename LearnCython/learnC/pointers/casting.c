#include <stdio.h>

int main(){
    int a = 1025;
    int *p = &a;
    printf("for p: address = %d, value = %d\n", p, *p);
    printf("for p+1: address = %d, value = %d\n", p+1, *(p+1));
    char *p2;
    p2 = (char*)p; // typecast to become a character pointer
    printf("for p2: address = %d, value = %d\n", p2, *p2); // when we dereference p2, we only see 1 byte because it is a char pointer
    // this is *p2 will be the binary of the first bit of the integer a
    printf("for p2+1: address = %d, value = %d\n", p2+1, *(p2+1)); // the byte after p2 will be the second byte of 1025 integer 
    // this which is 4 in binary
    void * p0 = p; // void pointer is a generic pointer, but this cannot be dereferenced
    // p0+1 is also not possible as there is not type, so it cannot increment like other data types' pointers
    return 0;
}