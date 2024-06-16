#include<iostream.h>
#include<conio.h>
void main()
{
char a;
clrscr();
cout<<"The value of A= ";
cin>>a;
if ((a=='A') || (a=='E') || (a=='I') || (a=='O') || (a=='U') || (a=='a') || (a=='e') || (a=='i') || (a=='o') ||(a=='u'))
{
cout<<"A is a vowel";
}
else
{
cout<<"A is not a vowel";
}
getch();
}