#include<iostream.h>
#include<conio.h>
class first
{
public:
void add()
{
int a,b,c;
a=20;
b=5;
c=a+b;
cout<<"Addition value= "<<c<<endl;
}
};

class second : public first
{
public:
void sub()
{
int p,q,r;
p=30;
q=5;
r=p-q;
cout<<"Subtraction value= "<<r<<endl
;
}
};

class third : public second
{
public:
void multi()
{
int x,y,z;
x=5;
y=5;
z=x*y;
cout<<"Multiplication value= "<<z<<endl;
}
};

void main()
{
third obj;
clrscr();
obj.add();
obj.sub();
obj.multi();
getch();
}

