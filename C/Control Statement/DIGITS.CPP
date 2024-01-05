#include<stdio.h>
#include<conio.h>
void main()
{
int i,x=0;
clrscr();
scanf("%d", &i);
while (i>0)
{
i=i/10;
x=x+1;
}
printf("%d",x);

getch();
}
