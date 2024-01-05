#include<iostream.h>
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
cin>>x;
cin>>y;
z=add(x,y);
cout<<z;
getch();
}
