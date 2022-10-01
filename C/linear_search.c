// Linear searching algorithm workflow in C
// Best Case: omega(1) which happened if somehow search key is in the begining of arrray
// Worst Case: big O(n) where n is the total number of elements in  array or size of the array
// It happened if the search element is in the last of the array or element not at all at array
#include<stdio.h>
int linear_search(int [], int, int);
int main()
{
    int i, array_size, key;
    printf("Enter the array size:\n");
    scanf("%d", &array_size);
    int arrays[array_size];
    printf("Enter arrays elements:\n");
    for (i=0;i<array_size;i++)
        scanf("%d", &arrays[i]);
    printf("Enter a number to search\n");
    scanf("%d", &key);
    int result = linear_search(arrays,array_size, key);
    if (result == 0)
        printf("Search Successful!");
    else
        printf("Can't find element inside array!");
    return 0;
}
int linear_search(int arrays[], int array_size, int key)
{
    int j;
    for (j=0;j<array_size;j++)
    {
        if (arrays[j] == key)
            return 0;
    }
    return -1;

}
