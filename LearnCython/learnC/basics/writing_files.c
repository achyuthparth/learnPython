#include <stdio.h>
#include <stdlib.h>

int main(){
    char line[255];
    FILE * f_pointer = fopen("sample.text", "w"); // creating a pointer which saves the memory address of the file on the computer
    fprintf(f_pointer, "This is a sample text. \nI am practicing writing to a file. \nI hope this works LOL"); // writes to file
    fclose(f_pointer); // w writes to a new file and overrides if the file exists
    FILE * f_pointer2 = fopen("sample.text", "a"); // a will append
    fprintf(f_pointer2, "\nThis is me appending"); 
    fclose(f_pointer2);
    FILE * f_pointer3 = fopen("sample.text", "r"); // r is for reading a file
    fgets(line, 255, f_pointer3); // will read first line and store it into line
    printf("%s", line);
    fgets(line, 255, f_pointer3); // this will get the second line
    printf("%s", line);
    fclose(f_pointer3); // do not forget to close
    return 0;
}