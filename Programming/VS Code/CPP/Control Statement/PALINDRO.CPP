#include<iostream.h>
#include<conio.h>
void main()
{
long int i,t,x=0,z;
clrscr();
cout<<"Enter I value= ";
cin>>i;
z=i;
while(i>0)
{
t=i%10;
x=((x*10)+t);
i=i/10;
}
cout<<x;
if(z==x)
{
cout<<"\n Palindrome";
}
else
{
cout<<"\n Not Palindrome";
}
getch();
}