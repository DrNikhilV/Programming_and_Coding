import java.util.*;
class Fib
{
public static void  main(String args[])
{
int a=0,b=1,c,i,n;
System.out.println("Enter a number - ");
Scanner sr = new Scanner(System.in);
n = sr.nextInt();
System.out.println(+a);
System.out.println(+b);
for(i=0;i<=n-3;i++)
{
c = a+b;
a=b;
b=c;
System.out.println(+c);
}

}
}
