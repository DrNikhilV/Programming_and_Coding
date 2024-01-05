#include<iostream.h>
#include<conio.h>
#include<fstream.h>
//using namespace std;
void main()
{
ofstream myfile("myfile.txt");
myfile<<"welcome to our CPP world";
myfile.close();
}
