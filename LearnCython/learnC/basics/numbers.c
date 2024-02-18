#include <stdio.h>
#include <stdlib.h>

int main(){
    /* regarding format specifiers for decimal numbers: 
    %f is for float (also double), 
    %lf is for double, 
    %Lf is for long double */
    printf("%f\n", 5 * 4.2); // Integer 5 was converted into floating point number
//  printf("%f", 5 * 4); This will not work because %f is for float, whereas the number is an integer
    printf("%f\n", 5 / 4); // This will output the quotient without the remainder
    printf("%f\n", 5 / 4.0); // This will output the decimal quotient
    printf("%f\n", pow(2, 3)); // C has some math functions by default like power here, does not with d%
    printf("%f\n", sqrt(3)); // By default the functions are set to integers
    printf("%f\n", ceil(3.6));
    printf("%f\n", floor(3.6));

    return 0;
}