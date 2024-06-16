//22038-Nikhil V
//Basic Operations
import java.util.*;
class One
{
public static void main(String args[])
{
int a,b,c;
System.out.println("Enter the value of a and b - ");
Scanner sr = new Scanner(System.in);
a = sr.nextInt();
b = sr.nextInt();
System.out.println("1.Addition");
System.out.println("2.Subtraction");
System.out.println("3.Multiplication");
System.out.println("4.Division");
System.out.println("5.Modulus");
c = sr.nextInt();
if(c == 1)
{
System.out.println("The value of a+b is "+(a+b));
}
if(c == 2)
{
System.out.println("The value of a-b is "+(a-b));
}
if(c == 3)
{
System.out.println("The value of a*b is "+(a*b));
}
if(c == 4)
{
System.out.println("The value of a/b is "+(a/b));
}
if(c == 5)
{
System.out.println("The value of a%b is "+(a%b));
}
}
}