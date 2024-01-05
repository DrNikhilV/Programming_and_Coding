#include<iostream.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
int main()
{
int gd=DETECT, gm,i,t,r,f,h;
initgraph(&gd, &gm, "C:\\Turboc3\\BGI");
t=200;
r=300;
f=50;
h=100;
for(i=1;i<700;i+=10)
{
line(t+i,t,t+i,400);
line(h+i,r,r+i,r);
circle(t+i,t,f);
circle(t+i,400,f);
circle(h+i,r,f);
circle(r+i,r,f);
line(t+i,t,h+i,r);
line(t+i,400,h+i,r);
line(t+i,t,r+i,r);
line(t+i,400,r+i,r);
delay(50);
cleardevice();
}
//rectangle(i,200,100,400);



delay(10);
//cleardevice();
getch();
//delay(100);
//cleardevice();
return 0;
//closegraph();
}
