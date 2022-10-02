//
#include<stdio.h>
int main()
{
    int p,t;
    float r,si,ta;
    printf("Enter principle:");
    scanf("%d",&p);
    printf("Enter time:");
    scanf("%d",&t);
    printf("Enter rate of interest:");
    scanf("%f",&r);
    si=(p*t*r)/100;
    ta=si+p;
    printf("Simple interest is %f",si);
    printf("\nTotal amount is %f",ta);
    return 0;
}

