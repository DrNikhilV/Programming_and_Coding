import java.io.*;
import java.util.Scanner;
class ElectricityBill
{
public static void main(String[]args)
{
int prev,curr,units,type;
double bill=0;
Scanner s=new Scanner(System.in);
System.out.println("Enter the type");
type=s.nextInt();
System.out.println("Enter the current and previous month reading");
curr=s.nextInt();
prev=s.nextInt();
units=curr-prev;
if(type==0)
{
if(units<=100)
bill=units*1;
else if(units>100 && units<=200)
bill=100+((units-100)*2.50);
else if(units>200 && units<=500)
bill=100+(100*2.50)+((units-200)*4);
else
bill=100+(100*2.50)+(300*4)+((units-500)*7);
}
else
{
if(units<=100)
bill=units*200;
else if(units>100 && units<=200)
bill=200+((units-100)*4.50);
else if(units>200 && units<=500)
bill=200+(100*4.50)+((units-200)*6);
else
bill=200+(100*4.50)+(300*6)+((units-500)*7);
}
System.out.println("BILL IS "+bill);
}
}
