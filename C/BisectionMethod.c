#include<stdio.h>
#include<conio.h>
#include<math.h>
#define f(x) exp(x)-4*sin(x) //define your function here 

int main()
{
	 float x0, x1, x2, f0, f1, f2, e;
	 int step = 1;
	 top:
	 printf("\nEnter initial and final guess:");
	 scanf("%f%f", &x0, &x1);
	 printf("Enter Error Tol:");
	 scanf("%f", &e);
	 f0 = f(x0);
	 f1 = f(x1);
	 if( f0 * f1 > 0.0)
	 {
		  printf("Invalid Initial Guesses.\n");
		  goto top;
	 }
	 printf("\nStep\t\tx0\t\tx1\t\tf0\t\tf1\t\tx2\t\tf(x2)\n");
	 do
	 {
		  x2 = (x0 + x1)/2;
		  f2 = f(x2);
		
		  printf("%d\t\t%f\t%f\t%f\t%f\t%f\t%f\n",step, x0, x1,f0,f1, x2, f2);
		
		  if( f0 * f2 < 0)
		  {
			   x1 = x2;
			   f1 = f2;
		  }
		  else
		  {
			   x0 = x2;
			   f0 = f2;
		  }
		  step = step + 1;
	 }while(fabs(f2)>e);
	 printf("\nRoot is: %f", x2);
	 return 0;
}