//strcmp() in C
//The strcmp() function compares two strings and return character by character and return 0 if both are equal
//strcmp(destination_string, source_string);
#include<stdio.h>
#include<string.h>
int main()
{
    char string1[20], string2[20];
    printf("Enter any two string to compare;\n");
    printf("First string: ");
    scanf("%s", string1);
    printf("Second string: ");
    scanf("%s", string2);
    int comparison = strcmp(string1, string2);
    if (comparison == 0) {
        printf("%d", comparison);
        printf("Both strings matched!");
    }
    else
    {
        printf("Both strings are different");
        printf("%d", comparison);
    }
    return 0;
}


