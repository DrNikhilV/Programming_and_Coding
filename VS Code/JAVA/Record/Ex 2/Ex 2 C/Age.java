import java.io.*;
import java.util.Scanner;
class Age
{ 
public static void main(String args[]) 
{
String name=new String();
Scanner s=new Scanner(System.in);
name=s.nextLine();
int age;
age=s.nextInt();
System.out.println(name+" Age is : "+age);
if(age<10)
System.out.println(name+" is a Kid");
else if(age>=10 && age<30)
System.out.println(name+" is young");
else if(age>=30)
System.out.println(name+" is a Senior");
} 
}
