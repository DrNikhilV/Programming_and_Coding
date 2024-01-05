#include<iostream.h>
#include<conio.h>
#include<math.h>
void main()
{
int a,b,c,d;
double r1,r2;
clrscr();
cout<<"The value of A= ";
cin>>a;
cout<<"The value of B= ";
cin>>b;
cout<<"The value of C= ";
cin>>c;
d=((b*b)-(4*a*c));
if(d>0)
{
r1=((-b + sqrt(d))/(2*a));
r2=((-b - sqrt(d))/(2*a));
}
else if(d<0)
{
r1=(-b/(2*a));
r2=(sqrt(a)/(2*a));
}
else
{
r1=(-b/(2*a));
r2=(-b/(2*a));
}
cout<<" r1 value= "<<r1;
cout<<"\n r2 value= "<<r2;
getch();
}