#include<iostream.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
int main()
{
int gd=DETECT, gm,i;
initgraph(&gd, &gm, "C:\\Turboc3\\BGI");
for(i=500;i>1;i=i-10)
{
line(200+i,200,400+i,200);
line(200+i,200,90+i,290);
line(400+i,200,450+i,290);
rectangle(30+i,290,450+i,370);
circle(100+i,380,40);
circle(400+i,380,40);



delay(40);
cleardevice();
}
//getch();
//delay(100);
//cleardevice();
return 0;
//closegraph();
}
