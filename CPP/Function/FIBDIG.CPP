#include<iostream.h>
#include<conio.h>

void add()

{
int a,b,c;
cout<<"Enter A value= ";
cin>>a;
cout<<"Enter B value= ";
cin>>b;
c=a+b;
cout<<"Value of C= "<<c<<endl;
}

void fib()

{
int n,i,a=0,b=1,c;
cout<<"Enter N value= "<<endl;
cin>>n;
for (i=1;i<=n;i++)
{
c=a+b;
a=b;
b=c;
cout<<"Fibonacci Series= "<<c<<endl;
}
}
void dig()

{
int i,x=0;
cout<<"Enter a number= "<<endl;
cin>>i;
while (i>0)
{
i=i/10;
x=x+1;
}
cout<<"Number of Digits= "<<x<<endl;
}

void main()
{
clrscr();
add();
fib();
dig();
getch();
}