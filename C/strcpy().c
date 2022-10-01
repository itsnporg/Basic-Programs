//strcpy() function
//strcpy(destination_string, source_string);
//like other data types string can't be copied or modified after declaration so that we use strcpy() function to
//copy source string to destination string
#include<stdio.h>
#include<string.h>
int main()
{
    char str1[20] = "to be copied string";
    char str2[20];
    strcpy(str2, str1);
    printf(str2);
    return 0;

}

