/*program to find Rootof a fuction by using Bisection method*/
#include <stdio.h>
#include <math.h>
#define MAX 100
#define E 0.00001
#define f(x) x *x - 4 * x - 10
int main()
{
   int count = 0;
   float x0, x1, x2, f0, f1, f2;
   printf("Enter the value of x1\n");
   scanf("%f", &x1);
   printf("Enter the value of x2\n");
   scanf("%f", &x2);
   f1 = f(x1);
   f2 = f(x2);
   if (f1 * f2 > 0)
      printf("Solution does not exit");
   else
   {
   begin:
      x0 = (x1 + x2) / 2;
      f0 = f(x0);
      if ((f1 * f0) < 0)
         x2 = x0;
      else
      {
         x1 = x0;
         f1 = f0;
      }
      if ((fabs(x2 - x1) / x1) < E)
      {
         x0 = (x1 + x2) / 2;
         printf("\nRoor=%f", x0);
         printf("\nFuctional value =%f", count);
         printf("\nIteration steps =%d", count);
      }
      else
      {
         count++;
         goto begin;
      }
   }
   return 0;
}