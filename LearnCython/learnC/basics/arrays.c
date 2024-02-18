#include <stdio.h>
#include <stdlib.h>

int main(){
    int int_array[10];
    int int_array2[] = {1, 2, 3};
    printf("%d\n", int_array2[1]);
    int_array2[1] = 7;
    printf("%d\n", int_array2[1]);
    printf("%d\n", int_array[0]); // will return 8???
    return 0;
}