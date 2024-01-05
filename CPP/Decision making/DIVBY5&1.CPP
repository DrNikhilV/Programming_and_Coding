#include<iostream.h>
#include<conio.h>
void main()
{
int a;
clrscr();
cout<<"The value of A= ";
cin>>a;
if(((a%5)==0) && ((a%11)==0))
{
cout<<"A is divisible";
}
else
{
cout<<"A is not divisible";
}
getch();
}