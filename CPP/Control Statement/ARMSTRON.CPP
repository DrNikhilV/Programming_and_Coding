#include<iostream.h>
#include<conio.h>
void main()
{
int i,j,k,x=0,y=0,z,a=1,b=0;
clrscr();
cout<<"Enter I value= ";
cin>>i;
z=i;
k=i;
while (i>0)
{
i=i/10;
x=x+1;
}
while(z>0)
{
a=1;
b=z%10;
for(j=0;j<x;j++)
{
 a=a*b;
}
y=y+a;
z=z/10;
}
if(k==y)
{
cout<<" It is a Armstrong number";
}
else
{
cout<<" Not a Armstrong number";
}
getch();
}
