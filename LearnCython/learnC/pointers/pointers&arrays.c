#include <stdio.h>

// arrays store the particular data type in consecutive byte locations
int main(){
    int array[5] = {1,2,3,4,5};
    int *p0 = &array[0];
    printf("location %i, value %i\n", p0, *p0);
    int *p1 = &array[1];
    printf("location %i, value %i\n", p1, *p1);
    int *p2 = p1 + 1;
    printf("location %i, value %i\n", p2, *p2);
    int *p = array; // simply using array without & will give the base address of the array aka element[0]
    printf("location %i, value %i\n", p, *p); // if u do not index the pointer definition, by default it will be the first element
    printf("location %i, value %i\n", p + 1, *(p+1));// we then increment the pointer to get next element
    printf("location %i, value %i\n", p + 2, *(p+2));
    printf("location %i, value %i\n", array, *array); // we can use the base address
    printf("location %i, value %i\n", array + 1, *(array + 1)); // we can also increment easily
    // p++ or array++ are both invalid as this would try to re-assign the pointer to the next value, when these point to base case
    return 0;
}