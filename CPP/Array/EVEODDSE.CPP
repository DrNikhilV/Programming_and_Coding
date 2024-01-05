#include<iostream.h>
#include<conio.h>
void main()
{
int a[100],d[100],c[100],i,n,x=0,y=0;
clrscr();
cout<<"Enter N value= ";
cin>>n;
for(i=0;i<n;i++)
{
cin>>a[i];
}
for(i=0;i<n;i++)
{
if ((a[i]%2)==0)
{
d[x]=a[i];
x=x+1;
}
else
{
c[y]=a[i];
y=y+1;
}
}
for (i=0;i<x;i++)
{
cout<<"Even="<<d[i]<<endl;
}
for (i=0;i<y;i++)
{
cout<<"Odd= "<<c[i]<<endl;
}
getch();
}
