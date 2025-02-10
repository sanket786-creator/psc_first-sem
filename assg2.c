#include<stdio.h>
int main()
{
float charge,cost;
printf("Enter the value of charge");
scanf("%f",&charge);
if(charge>=1 && charge<=200)
{
    cost=(0.50*charge);
    printf("%f",cost);
}
if(charge>=201 && charge<=400)
{
    cost=(100+((charge-200)*0.65));
    printf("%f",cost);
}
if(charge>=401 && charge<=600)
{
    cost=(230+((charge-400)*0.80));
    printf("%f",cost);
}
if(charge>=601)
{
    cost=(390+((charge-600)*1));
    printf("%f",cost);
}
}