// Check leap year
// For leap year entered year should be perfectly divided by 4
// For centuries leap year should be perfectly divided by 400
#include<stdio.h>
int main()
{
    int year;
    printf("Enter the year;\n");
    scanf("%d", &year);
    if ((year % 4 == 0) || (year % 400 == 0))
        printf("%d is leap year\n", year);
    else
        printf("%d isn't leap year\n", year);
    return 0;
}

