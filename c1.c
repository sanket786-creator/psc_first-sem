#include<stdio.h>
int main()
{
int sum,m,isPrime,l,j,i,n,count,count1;
printf("Enter a number");
scanf("%d",&n);
i=0;
j=0;
sum=0;
count=0;
count1=0;
do
{
i=i+1;
printf("%d ",i);
sum=sum+i;
}
while(i<n);
printf("\n");
printf("The sum is %d\n",sum);
i=0;
printf("Evennumbers");
do
{
i=i+1;
if(i%2==0)
{
printf("\n%d",i);
count=count+1;  
}
}
while(i<n);
printf("\noddnumbers");
do
{
j=j+1;
if(j%2!=0)
{
printf("\n%d",j);
count1=count1+1;
}
}
while(j<n);
printf("\n");
printf("Even numbers is %d\n",count);
printf("Odd number is %d\n",count1);
printf("prime numbers");
m = 2;
do 
{
isPrime =1;
l = 2;
while (l <= m / 2) 
{
if (m % l == 0) 
{
isPrime = 0;  // Set isPrime to 0 if i is divisible by j
break;
}
l=l+1;
}
 // If isPrime is still 1, then i is a prime number
if (isPrime == 1) 
{
printf("%d ", m);
}
m=m+1;  // Move to the next number
} 
while (m<=n);
printf("\n");
}
