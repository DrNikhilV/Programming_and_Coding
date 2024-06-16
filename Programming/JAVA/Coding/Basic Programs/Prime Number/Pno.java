import java.util.*;
class Pno
{
public static void  main(String args[])
{
int a=0,n,i;
System.out.println("Enter a number - ");
Scanner sr = new Scanner(System.in);
n = sr.nextInt();
for(i=2;i<n;i++)
{
if (n%i == 0)
{
a++;
}
}
if ( a >= 1)
{
System.out.println(" No ");
}
else
{
System.out.println(" Yes ");
}
}
}
