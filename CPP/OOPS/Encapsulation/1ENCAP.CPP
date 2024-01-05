#include<iostream.h>
#include<conio.h>
class cl1
{
private:
int sal;
public:
void setSal(int x)
{
sal=x;
}
int getSal()
{
 return sal;
}

};
void main()
{
cl1 obj1;
clrscr();
obj1.setSal(100);
cout<<obj1.getSal();
getch();
}
