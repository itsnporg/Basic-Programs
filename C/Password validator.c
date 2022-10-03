#include <stdio.h>
#include<string.h>
int main() {
char s[10];
int sy=0,cap=0,num=0,i;
scanf("%s",s);
printf("Password is %s\n",s);
if(strlen(s)>5 && strlen(s)<10)
{
    for(i=0;i<strlen(s);i++)
    {
        if(s[i]>65 && s[i]<91)
          cap++;
        else if(s[i]>48 && s[i]<57)
          sy++;
        else if(s[i]<97 || s[i]>123)
          num++;
    }
    if(sy==0 || cap==0 || num==0){
    printf("A strong password must be between 5-10 charcters and must contain atleast 1 or more symbols,capital letters,numbers");}
    else
      printf("Password is valid");
}
else 
printf("Password is not between 5-10 characters");
    return 0;
}
