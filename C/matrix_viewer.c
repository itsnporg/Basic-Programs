// View entered 2*2 matrix in console
#include<stdio.h>
int main()
{
    int element_first[2], element_second[2], result, i, j;
    for (i = 0; i<2; i++)
    {
        for (j=0; j<2; j++)
        {
            printf("Enter the first element: ");
            scanf("%d",&element_first[i]);
            printf("Enter the second element: ");
            scanf("%d",&element_second[i]);
        }

    }


    for (i = 0; i<2; i++)
    {
        printf("%d\t", element_first[i]);
        printf("%d\t\n", element_second[i]);
    }
    return  0;
}
