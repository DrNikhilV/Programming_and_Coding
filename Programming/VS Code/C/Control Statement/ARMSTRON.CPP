#include<stdio.h>
#include<conio.h>
void main()
{
int s,i,x=0,z,t=0,a=1,j,y=0;
clrscr();
scanf("%d", &i);
z=i;
s=i;
while (i>0)
{
i=i/10;
x=x+1;
}
while(z>0)
{
a=1;
t=z%10;
for(j=0;j<x;j++)
{
 a=a*t;
}
y=y+a;
z=z/10;
}
if(s==y)
{
printf(" It is a Armstrong number");
}
else
{
printf(" Not a Armstrong number");
}
getch();
}
