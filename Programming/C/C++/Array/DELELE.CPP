#include<iostream.h>
#include<conio.h>
void main()
{
int a[100],i,n,x,y;
clrscr();
cout<<"Enter N value= ";
cin>>n;
for(i=0;i<n;i++)
{
cin>>a[i];
}
for(i=0;i<n;i++)
{
cout<<a[i];
}
cout<<"Enter Position";
cin>>x;
for(i=x-1;i<n;i++)
{
a[i]=a[i+1];
}
a[i]=y;
n=n-1;
for(i=0;i<n;i++)
{
cout<<a[i]<<endl;
}
getch();
}