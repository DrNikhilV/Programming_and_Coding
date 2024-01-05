#include<iostream.h>
#include<conio.h>
void main()
{
long int i,t,x=0;
clrscr();
cout<<"Enter I value= ";
cin>>i;
while(i>0)
{
t=i%10;
x=((x*10)+t);
i=i/10;
}
cout<<x;
getch();
}