#include <stdio.h>

//prototyping methods
int sum_elements(int a[], int size);

int main(){
    int a[] = {1,2,3,4,5};
    int size = sizeof(a)/sizeof(a[0]);
    int total = sum_elements(a, size); // send pointer of the array
    printf("sum is %d\n", total);
    return 0;
}

int sum_elements(int a[], int size){
    int i, sum = 0;
    for (i = 0; i < size; i++){
        sum += a[i];
    } return sum;
}