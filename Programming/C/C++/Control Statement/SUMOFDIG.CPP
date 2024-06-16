#include<iostream.h>
#include<conio.h>
void main()
{
int i,t,x=0;
clrscr();
cout<<"Enter I value= ";
cin>>i;
while(i>0)
{
t=i%10;
x=x+t;
i=i/10;
}
cout<<x;
getch();
}