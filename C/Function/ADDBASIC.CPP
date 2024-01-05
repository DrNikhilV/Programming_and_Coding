#include<stdio.h>
#include<conio.h>
int add(int a, int b)
{
int c;
c=a+b;
return c;
}
void main()
{
int x,y,z;
clrscr();
scanf("%d",&x);
scanf("%d",&y);
z=add(x,y);
printf("%d",z);
getch();
}
