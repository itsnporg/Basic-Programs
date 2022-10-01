/* Function to add, sub, multiply, divide two complex number(x+iy) and 
(a+ib)*/

#include<stdio.h> 
void add(int,int,int,int); 
void sub(int,int,int,int); 
void mul(int,int,int,int); 
void div(float,float,float,float); 
int main() 
{ 
	int x,y,c,d;
	printf("Enter real and imaginary part 1:\n"); 
	scanf("%d%d",&x,&y); 
	printf("Enter real and imaginary part 2:\n"); 
	scanf("%d%d",&c,&d); 
	add(x,y,c,d); 
	sub(x,y,c,d); 
	mul(x,y,c,d); 
	div(x,y,c,d); 
	return 0; 
} 


void add(int x,int y, int c,int d) 
{ 
	int realsum,imgsum; 
	realsum=x+c; 
	imgsum=y+d; 
	printf("The sum of complex numbers=%d+i(%d)\n",realsum,imgsum); 
} 


void sub(int x,int y, int c,int d) 
{ 
	int real,img; 
	real=x-c; 
	img=y-d; 
	printf("The subtraction of complex numbers=%d+i(%d)\n",real,img); 
} 


void mul(int x,int y, int c, int d) 
{ 
	int real, img; 
	real=(x*c-y*d); 
	img=(x*d+y*c);
	printf("The multiplication of complex numbers=%d+i(%d)\n",real,img); 
} 


void div(float x,float y, float c,float d) 
{ 
	float real,img; 
	real=(x*c+y*d)/(c*c+d*d); 
	img=(y*c-x*d)/(c*c+d*d) ; 
	printf("The division of complex numbers=%f+i(%f\n)",real,img); 
}

