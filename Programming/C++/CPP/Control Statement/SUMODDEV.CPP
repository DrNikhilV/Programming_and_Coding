#include<iostream.h>
#include<conio.h>
void main()
{
int i,n,x=0,y=0;
clrscr();
cout<<"Enter n value= ";
cin>>n;
for(i=0;i<=n;i++)
{
if((i%2)==0)
{
cout<<"Even= "<<i<<endl;
x=x+i;
}
else
{
cout<<"Odd= "<<i<<endl;
y=y+i;
}
}
cout<<"Even sum="<<x<<endl;
cout<<"Odd sum="<<y<<endl;
getch();
}