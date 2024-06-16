#include<iostream.h>
#include<conio.h>
void main()
{
int i,x=0;
clrscr();
cout<<"Enter I value= ";
cin>>i;
while(i>0)
{
i=i/10;
x=x+1;
}
cout<<x;
getch();
}