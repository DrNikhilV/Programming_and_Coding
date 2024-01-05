#include<iostream.h>
#include<conio.h>
void main()
{
int a[100],i,n,j,t;
clrscr();
cout<<"Enter N value= ";
cin>>n;
for(i=0;i<n;i++)
{
cin>>a[i];
}
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(a[i]<a[j])
{
t=a[i];
a[i]=a[j];
a[j]=t;
}
}
}
cout<<"Ordered list"<<endl;
for(i=0;i<n;i++)
{
cout<<a[i]<<endl;
}
getch();
}



