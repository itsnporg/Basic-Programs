// Example of insertion sort in C
#include<stdio.h>
int main()
{
    int i, j, key, n;
    int our_array[] = {5,4,3,2,1,11,22,4,5};
    for (j=0; j<9; j++)
    {
        key = our_array[j];
        i = j-1;

        while (i>=0 && key<our_array[i])
        {
            our_array[i+1] = our_array[i];
            i--;
        }
        our_array[i+1] = key;
    }
    for (j=0; j<9; j++)
        printf("%d ", our_array[j]);

}
