#include<iostream.h>
#include<conio.h>
void main()
{
int a[100],i,n,x;
clrscr();
cout<<"Enter N value= ";
cin>>n;
for(i=0;i<n;i++)
{
cin>>a[i];
}
cout<<"Enter Element";
cin>>x;
for(i=0;i<n;i++)
{
if (a[i]==x)
{
cout<<"Element Found";
}
}
getch();
}