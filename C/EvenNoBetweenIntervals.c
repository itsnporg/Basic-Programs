#include<stdio.h>
main()
{
    int a,b,i;
    printf("Enter the intevals ::\n");
    scanf("%d\n%d",&a,&b);
    printf("The even numbers are ::\n");
    for(i=a;i<=b;i++)
    {
        if(i%2==0)
        {
            printf("%d\n",i);
        }
    }
}
