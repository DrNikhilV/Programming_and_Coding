#include<iostream.h>
#include<conio.h>
/* Class 1 */
class cl1
{
private:
int sal;
public:
int b;
void setSal(int x)
{
sal=x;
}
int getSal()
{
 return sal;
}
};
/* Class 2*/
class cl2
{
private:
int cal;
public:
void setCal(int y)
{
cal=y;
}
int getCal()
{
return cal;
}
};
void main()
{
cl1 obj1;
cl2 obj2;
clrscr();
obj1.setSal(100);
obj2.setCal(200);
obj1.b=1000;
cout<<obj1.getSal();
cout<<obj2.getCal();
cout<<obj1.b;
getch();
}
