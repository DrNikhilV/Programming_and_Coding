#include<stdio.h>
#include<conio.h>
void main()
{
int i,x=0,t;
clrscr();
scanf("%d", &i);
while (i>0)
{
t=i%10;
x=(x*10)+t;
i=i/10;
}
printf("%d",x);

getch();
}
