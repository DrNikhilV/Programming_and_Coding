#include<iostream.h>
#include<conio.h>
void main()
{
int n,y,i,x=0;
clrscr();
cout<<"Enter N value= ";
cin>>n;
for (i=2;i<=n;i++)
if ((n%i)==0)
{
x=x+1;
}
if (x>1)
{
cout<<"It is not a prime number";
}
else
{
cout<<"It is a prime number";
}
getch();
}













































