#include<stdio.h>
int main()
{
float x,y,z,w;
printf("Enter value of x");
scanf("%e",&x);
printf("Enter value of y");
scanf("%e",&y);
z=((x+y)/(x-y));
if((x-y)==0)
{
printf("undefined");
}
else
{
printf("%e",z);
}
z=((x+y)*(x-y));
printf(" %0.1e",w);
}