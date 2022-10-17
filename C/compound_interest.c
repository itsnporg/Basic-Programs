#include <stdio.h>
#include <math.h>

int main(void){
    double principal, rate, amount;
    int years, i;

    printf("Enter the principal: ");
    scanf("%lf", &principal);
    printf("Enter the rate: ");
    scanf("%lf", &rate);
    printf("Enter the number of years: ");
    scanf("%d", &years);

    printf("Year\tAmount on deposit \n");

    for (i = 1; i <= years; i++){
        amount = principal * pow(1 + rate, i);
        printf("%d\t%.2f \n", i, amount);
    }

    return 0;
}