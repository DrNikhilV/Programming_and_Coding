//Nikhil V
//22038
import java.util.*;
class Sum
{
public static void main(String args[])
{
int i=0,n,temp;
System.out.println("Enter a number - ");
Scanner sr = new Scanner(System.in);
n = sr.nextInt();
while(n!=0)
{
    temp = n%10;
    i = i + temp;
    n = n/10;
}
System.out.println(+i);
}
}