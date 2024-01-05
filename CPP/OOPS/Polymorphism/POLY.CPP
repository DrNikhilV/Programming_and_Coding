#include<iostream.h>
#include<conio.h>
class first
{
public:
void add(int a, int b)
{
int c;
c=a+b;
cout<<"Addition value= "<<c<<endl;
}
};

class second : public first
{
public:
void add(float p, float q)
{
float r;
r=p-q;
cout<<"Subtraction value= "<<r<<endl;
}
};

/*class third : public second
{
public:
void add(char x)
{
switch(x)
{
 value 'a':
 value 'e':
 value 'i':
 value 'o':
 value 'u':
	cout<<"The given character is vovel"<<x;
	break;
 default:
	cout<<"The given character is not a vovel"<<x;
 }
 }
};*/

void main()
{
second obj;
clrscr();
obj.add(6, 5);
obj.add(6.5, 10.8);
//char d='a';
//obj.add(d);
getch();
}

