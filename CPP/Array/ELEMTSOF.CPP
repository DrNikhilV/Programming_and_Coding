#include<iostream.h>
#include<conio.h>
void main()
{
int a[100],i,n;
clrscr();
cout<<"Enter N value= ";
cin>>n;
for(i=0;i<n;i++)
{
cin>>a[i];
}
for(i=0;i<n;i++)
{
cout<<a[i]<<endl;
}
getch();
}