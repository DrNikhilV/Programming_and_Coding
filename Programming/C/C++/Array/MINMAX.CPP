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
if(a[i]>a[j])
{
t=a[i];
a[i]=a[j];
a[j]=t;
}
}
}
for(i=0;i<n;i++)
{
cout<<a[i]<<endl;
}
cout<<"Min= "<<a[0];
cout<<"Max= "<<a[n-1];
getch();
}



