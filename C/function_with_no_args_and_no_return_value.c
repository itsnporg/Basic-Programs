#include <stdio.h>

void area_of_rectangle();
void main(){
    printf("Before Function Call \n");
    area_of_rectangle();
    printf("After Function Call");
}

void area_of_rectangle(){
    int area, length, breadth;
    printf("Enter length and breadth of a rectangle : ");
    scanf("%d%d",&length,&breadth);
    area = length * breadth;
    printf("Area of Rectangle is : %d \n", area);
}
