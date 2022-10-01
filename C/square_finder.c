//Program to find square upto 6th term starting from 10 and decreasing it
#include<stdio.h>
int main()
{
	int a,b=10;
	a=6;
	while(a>0)
	{
		printf("%d \n",b*b);
		b --;
		a--;
	}
	return 0;
}
