#include <iostream.h>
#include <conio.h>
void add(int a, int b)
{
int c;
c=a+b;
cout<<"The addition value is = "<<c;
}
void add(double a, double b)
{
double d;
d=a*b;
cout<<"\nThe multiplication value is = "<<d;
}
void add(char a)
{
char x=a;
if((x=='a')|| (x=='e') || (x=='i') || (x=='o') || (x=='u'))
{
cout<<"Vowel"<<endl;
}
else
{
cout<<"consonant"<<endl;
}
}
void main()
{
clrscr();
add(6,5);
add(10.1,12.2);
add('c');
getch();
}