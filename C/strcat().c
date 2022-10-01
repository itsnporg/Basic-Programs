//strcat() in C
//The strcat() function combines both string
//strcat(destination_string, source_string);
//NOTE: It save combined string is destination string or first argument string
#include<stdio.h>
#include<string.h>
int main()
{
    char string1[20], string2[20];
    printf("Enter any two string to conceinate;\n");
    printf("First string: ");
    scanf("%s", string1);
    printf("Second string: ");
    scanf("%s", string2);
    strcat(string1, string2);
    printf("The combined string is %s", string1);
    return 0;

}
