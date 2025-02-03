#include<stdio.h>
void main()
{
printf("Hello Sanket");
}

#include<stdio.h>
int main()
{
printf("my Biodata\n");
printf("\n");
printf("Name:-Sanket Gavkari\n");
printf("Father Name:-Sachin Gavkari\n");
printf("Mother Name:-Anuradha Gavkari\n");
printf("DOB:-DD/MM/2006\n");
printf("Address:-Asara,jule solapur,soalpur-413004\n");
printf("University Name:-MIT Vishwaprayag University\n");
printf("Educational detail:-Studying B.Tech at MIT-VPU");
printf("Phone Number:-8767XXXXXX\n");
printf("Email id:-........@gmail.com");
}

// #include<stdio.h>
// int main()
// {
// int a,b;
// a=43;
// b=6;
// printf("The value of a-b is %d",a-b);
// 
// format operator for float is %f. if wrong format specifier error occurs

// increment decrement operator
// #include<stdio.h>
// int main()
// {
// int m=5;
// int y;
// y=++m;
// printf("the value of m is %d and value of y is %d",m,y);
// y=m++;
// printf("the value of m is %d and value of y is %d",m,y);
// }

//write a program to display equation of the line in form of ax+by=c a=5,b=8,c=18

#include<stdio.h>
int main()
{
int a=5,b=8,c=18;
printf("%dx+%dy=%d",a,b,c);
}
// format specifier takes values in sequence i.e, first %d takes a second takes b and third ta


// #include<stdio.h>
// main()
// {
// float a,b,c,y,x,z;
// a=9;
// b=12;
// c=3;
// x=a-b/3+c*2-1;
// y=a-b/(3+c)*(2-1);
// z=a-(b/(3+c)*2)-1;
// printf("x=%0.1f\n",x);
// printf("y=%0.1f\n",y);
// printf("y=%0.1f\n",z);
// }
//many zero come after decimal so using 0.1 it will show only one digit after decimal

//write a program that read the value of distance travelled by car and time taken for same.compute speed
#include<stdio.h>
int main()
{
int distance,time,speed;
printf("enter the value of distance in km");
scanf("%d",&distance);
printf("enter the value of time in minutes");
scanf("%d",&time);
speed=distance/time;
printf("The value of speed is %dkm/min",speed);
}


