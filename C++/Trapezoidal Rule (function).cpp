/*program to find Integration of given funtion by using Trapezoidal rule*/
#include<stdio.h>
#include<conio.h>
#include<math.h>
#define f(x) x*x*x+1
void main()
{
	clrscr();
   float a,b,h,It;
   printf("\nEnter initial value of X:");
   scanf("%f",&a);
   printf("\nEnter  Final  value of X:");
   scanf("%f",&b);
   h=(b-a)/2;
   It =h*(f(a)+f(b));
   printf("\nThe integration value of function :%f",It);
   getch();
}
