#include<iostream.h>
#include<conio.h>
void main()
{
int * a;
int b;
clrscr();
cout<<"Enter B value= ";
cin>>b;
a=&b;
cout<<"Location of B= "<<a<<endl;
getch();
}