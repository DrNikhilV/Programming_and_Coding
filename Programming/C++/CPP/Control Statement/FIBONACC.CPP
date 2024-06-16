#include<iostream.h>
#include<conio.h>
void main()
{
int i,n,a=0,b=1,c;
clrscr();
cout<<"Enter N value= ";
cin>>n;
for(i=1;i<=n;i++)
{
c=a+b;
a=b;
b=c;
cout<<"Fibonacci Series= "<<c<<endl;
}
getch();
}
