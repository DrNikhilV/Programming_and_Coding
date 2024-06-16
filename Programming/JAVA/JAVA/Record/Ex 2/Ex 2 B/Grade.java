import java.io.*;
class Grade
{ 
public static void main(String args[]) 
{
 String name=new String("BALAJI");
int rno,m1,m2,m3,m4,m5;
float Avg;
rno=1101;
 m1=90;
 m2=94;
 m3=89;
 m4=95; 
 m5=96;
Avg=(m1+m2+m3+m4+m5)/5;
if(Avg>90 &&Avg<=100)
System.out.println("Grade of "+name+" is S");
else if(Avg>80 &&Avg<=90)
System.out.println("Grade of "+name+" is A");
else if(Avg>70 &&Avg<=80)
System.out.println("Grade of "+name+" is B");
else if(Avg>60 &&Avg<=70)
System.out.println("Grade of "+name+" is C");
else if(Avg>50 &&Avg<=60)
System.out.println("Grade of "+name+" is D");
else
System.out.println("Grade of "+name+" is U");
} 
}
