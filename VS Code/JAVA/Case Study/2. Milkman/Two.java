import java.util.*;
class Twoo
{
public static void main(String args[])
{
int a,sum=0,sum1=0,sum2=0;
System.out.println("Enter the amount of Milk : ");
Scanner sr = new Scanner(System.in);
a = sr.nextInt();

System.out.println("The amount of cans required is : ");
while(a>0)
{
if(a>=5)
{
sum = a/5;
a = a%5;
if(a%5 == 0)
{
    a = 0;
}
}
if(a>=3)
{
sum1 = a/3;
a = a%3;
if(a%3 == 0)
{
    a = 0;
}
}
if(a>=1)
{
    sum2+= a;
a = a%a;
}
}

System.out.println("5L cans "+sum);
System.out.println("3L cans "+sum1);
System.out.println("1L cans "+sum2);

}
}