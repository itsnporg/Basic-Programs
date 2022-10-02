//Matrix calculator
//Operation: Divide, Multiply, Addition, Subtraction
#include<stdio.h>
int main()
{
	int row, coloumn, i, j;
	char ch;
	printf("\t\t----------------MATRIX OPERATION------------");
	printf("\n\nEnter the number of rows of matrix;\n");
	scanf("%d", &row);
	printf("Enter the number of columns of matrix;\n");
	scanf("%d", &coloumn);
	int a[row][coloumn], b[row][coloumn], c[row][coloumn];
	printf("\nEnter the elements of first matrix;\n");
	for (i=0; i<row; i++)
	{
		for(j=0; j<coloumn; j++)
		{
			scanf("%d", &a[i] [j]);
		}
	}
	
	printf("\nEnter the elements of second matrix;\n");
	for (i=0; i<row; i++)
	{
		for(j=0; j<coloumn; j++)
		{
			scanf("%d",&b[i] [j]);
		}
	}
	
	printf("\nEnter the operator to do calculation;\n");
	printf("\n'+' for addition\n'-' for subtraction\n'*' for multipication \n'/' for division;\n");
	scanf(" %c", &ch);
	printf("\nThe Result is;\n");
	
	if (ch == '+')
		{	
			for (i=0; i<row; i++)
			{
				for(j=0; j<coloumn; j++)
				{
					c[i] [j] = a[i] [j] + b[j] [j];
					printf("%d\t", c[i] [j]);
				}
				printf("\n");
			}	
			return 0;
		
	}
		
	
		else if (ch == '-')
		{
			for (i=0; i<row; i++)
			{
				for(j=0; j<coloumn; j++)
				{
					c[i] [j] = a[i] [j] - b[i] [j];
					printf("%d\t", c[i] [j]);
				}
				printf("\n");
			}	
			return 0;
		}
		
		
		else if (ch == '/')
		{	
			for (i=0; i<row; i++)
			{
				for(j=0; j<coloumn; j++)
				{
					c[i] [j] = a[i] [j] / b[i] [j];
					printf("%d\t", c[i] [j]);
				}
				printf("\n");
			}	
			return 0;
		}
		
		else if (ch == '*')
		{	
			for (i=0; i<row; i++)
			{
				for(j=0; j<coloumn; j++)
				{
					c[i] [j] = a[i] [j] * b[i] [j];
					printf("%d\t", c[i] [j]);
				}
				printf("\n");
			}	
			return 0;
		}
		
		else
			printf("Invalid Operator --> %c", ch);
		
}


