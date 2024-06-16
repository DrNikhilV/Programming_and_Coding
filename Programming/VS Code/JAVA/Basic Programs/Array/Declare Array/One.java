import java.util.*;
class One
{
public static void main(String args[])
{
int num;
System.out.println("Enter size of array : ");
Scanner sr = new Scanner(System.in);
num = sr.nextInt();
int a[] = new int[num];
int i,j;
System.out.println("Enter the array : ");
for(i=0;i<num;i++)
{
a[i] = sr.nextInt();
}
for(i=0;i<num;i++)
{
System.out.println(a[i]);
}
}
}
