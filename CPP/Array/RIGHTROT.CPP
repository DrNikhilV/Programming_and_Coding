#include<iostream.h>
#include<conio.h>
void main()
{
int a[100],i,n,j,x,t;
clrscr();
cout<<" No of Elements= ";
cin>>n;
for(i=0;i<n;i++)
{
cin>>a[i];
}
cout<<"No of times to be rotated= ";
cin>>x;
for(i=0;i<x;i++)
{
t=a[0];
{
for(j=0;j<n;j++)
{
a[j]=a[j+1];
}
a[j-1]=t;
}
}
for(i=0;i<n;i++)
{
cout<<a[i]<<endl;
}
getch();
}