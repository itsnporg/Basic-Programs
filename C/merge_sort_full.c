//Merge sort in practical C
// Use recursion/Divide and Conquer
// It use more memory but it is more faster than other sorting algorithm
// Worst Case: Bih O(log n)
// Best Case: Omega(log n)
// it's Big thita (log n) cause best case and worst case are same
#include<stdio.h>
# define max 100
void merger(int [], int, int);
void merge_it(int [], int, int, int);
void display(int[], int);
int main()
{
    int arrays[max],l=0,n,i;
    printf("Enter Array size;\n");
    scanf("%d", &n);
    int h = n-1;
    printf("Enter the elements;\n");
    for (i=0;i<n;i++)
    {
        scanf("%d", &arrays[i]);
    }
    merger(arrays,l,h);
    display(arrays,h);

}
void display(int arrays[],int h)
{
    int i;
    for (i=0;i<=h;i++)
    {
        printf("%d\t", arrays[i]);
    }
}
void merger(int arrays[], int l, int h)
{
    if (l<h)
    {
        int mid = (l+h)/2;
        merger(arrays,l,mid);
        merger(arrays,mid+1,h);
        merge_it(arrays, l, mid, h);
    }
}
void merge_it(int arrays[], int l, int mid, int h)
{
    int k;
    int arrays_b[max];
    int i = l;
    int j = mid+1;
    for (k=l; k<=h; k++)
    {
        if (i>mid)
        {
            arrays_b[k] = arrays[j];
            j ++;
        }
        else if (j>h)
        {
            arrays_b[k] = arrays[i];
            i ++;
        }
        else if (arrays[i] <= arrays[j])
        {
            arrays_b[k] = arrays[i];
            i ++;
        }
        else if (arrays[i] >= arrays[j])
        {
            arrays_b[k] = arrays[j];
            j ++;
        }
    }
    for (k=l; k<=h; k++)
        arrays[k] = arrays_b[k];
}