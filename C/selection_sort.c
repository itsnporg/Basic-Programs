
#include <stdio.h>
// void selection_sort(int a[100],n;

int main()
{
   int n = 4, i, j, temp, iMin;
   // Enter array values
   int unsorted[] = {1, 6, 9, 0};
   for (i = 0; i < n - 1; i++)
   {
      iMin = i;
      for (j = i + 1; j < n; j++)
      {
         if (unsorted[j] < unsorted[iMin])
            iMin = j;
      }
      temp = unsorted[i];
      unsorted[i] = unsorted[iMin];
      unsorted[iMin] = temp;
   }

   for (i = 0; i < n; i++)
   {
      // printf("Inner loop");
      printf("%d", unsorted[i]);
   }
   return 0;
}