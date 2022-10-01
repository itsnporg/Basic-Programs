#include<stdio.h>
int main()
{
    int n[20],i,max,min;
    for(i=0;i<20;i++)
    {
        printf("Enter any 20 numbers:");
        scanf("%d",&n[i]);
    }
//finding greatest and smallest
    max=n[0];
    min=n[0];
    for(i=0;i<20;i++)
    {
        if(n[i]>max)
            max=n[i];
        if(n[i]<min0
            min=n[i];
    }
    printf("The biggest number=%d\n",max);
    printf("The smallest number=%d",min);
    return 0;
}
