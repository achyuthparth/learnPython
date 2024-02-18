#include <stdio.h>
#include <stdlib.h>

int main(){
    int j;
    for (j = 1; j <= 5; j ++) {printf("%d\n", j);}
    
    int int_array[] = {1, 2, 3, 4, 5, 6};
    int i;
    for (i = 0; i < 6; i++) {printf("%d\n", int_array[i]);}
    return 0;
}