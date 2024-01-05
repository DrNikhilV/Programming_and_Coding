#include<iostream.h>
#include<conio.h>
void main()
{
long int n,i,j,x;
clrscr();
cout<<"Enter N value= ";
cin>>n;
for(i=1;i<=n;i++)
{
x=1;
for(j=1;j<=i;j++)
{
x=x*i;
}
}
cout<<"Answer= "<<x;
getch();
}