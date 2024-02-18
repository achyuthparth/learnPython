#include <stdio.h>
#include <stdlib.h>

int main(){
    int num = 5;
    printf("%d\n", num);
    num = 8;
    printf("%d\n", num); // these can be modified
    const int num2 = 9; // these cannot be modified as these are constants
    printf("%d\n", num2); // generally C programmers use capitals for constants
    // objects in the printf parameter are also considered constants
    return 0;
}