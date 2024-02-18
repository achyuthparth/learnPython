#include <stdio.h>
#include <stdlib.h>

int main(){
    char color[20];
    printf("Enter a color: \n");
    scanf("%s", color); // why no pointer?
    char plural_noun[20];
    printf("Enter a plural noun: \n");
    scanf("%s", plural_noun);
    char person[20];
    char person2[20];
    printf("Enter a person's first and last name: \n");
    scanf("%s%s", person, person2);

    printf("Roses are %s,\n", color);
    printf("%s are blue,\n", plural_noun);
    printf("I love %s %s.\n", person, person2);
    return 0;
}