import java.io.*;
class Room
{
int len;
int breadth;
Room(int x,int y)
{
len=x;
breadth=y;
}
int area()
{
return(len * breadth);
}
}
ClassBedRoom extends Room
{
int height;
BedRoom(intx,inty,int z)
 {
super(x,y);
height=z;
 }
int volume()
 {
return (len*breadth*height);
 }
}

Class InherTest
{
public static void main(String args[])
{
BedRoom B=new BedRoom(20,15,10);
int area1=B.area();
int vol1=B.volume();
System.out.println("Area of the room is : "+area1);
System.out.println("Volume of the room is : "+vol1);
}
}