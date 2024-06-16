#include<iostream.h>
#include<conio.h>
void main()
{
int a[100],i,n,j,x=0;
clrscr();
cout<<"Enter N value= ";
cin>>n;
for(i=0;i<n;i++)
{
cin>>a[i];
}
for(i=0;i<n;i++)
{
if (a[i]<0)
{
x=x+1;
}
}
cout<<"No of Negative= "<<x;
getch();
}