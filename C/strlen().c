//using strlen() function
#include<stdio.h>
#include<string.h>
int main()
{
    char name[20];
    printf("Enter a string\n");
    scanf("%s", name);
    int len = strlen(name);
    printf("The length is %d", len);
    return 0;
}

