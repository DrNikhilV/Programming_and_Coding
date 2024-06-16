#include<iostream.h>
#include<conio.h>
void main()
{
int a[100],d[100],c[100],i,n,x=0,y=0,j,t,s;
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
for(j=i+1;j<x;j++)
{
if(d[i]>d[j])
{
t=d[i];
d[i]=d[j];
d[j]=t;
}
}
cout<<"Even= "<<d[i]<<endl;
}
for (i=0;i<y;i++)
{
for(j=i+1;j<y;j++)
{
if(c[i]>c[j])
{
s=c[i];
c[i]=c[j];
c[j]=s;
}
}
cout<<"Odd= "<<c[i]<<endl;
}
getch();
}
