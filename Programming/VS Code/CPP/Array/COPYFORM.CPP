#include<iostream.h>
#include<conio.h>
void main()
{
int a[100],b[100],i,n;
clrscr();
cout<<"Enter N value= ";
cin>>n;
for(i=0;i<n;i++)
{
cin>>a[i];
}
for(i=0;i<n;i++)
{
b[i]=a[i];
cout<<"Array A= "<<a[i];
cout<<"Array B= "<<b[i]<<endl;
}
getch();
}