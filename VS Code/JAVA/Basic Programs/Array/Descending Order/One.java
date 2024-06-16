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
int i,j,temp;
System.out.println("Enter the array : ");
for(i=0;i<num;i++)
{
a[i] = sr.nextInt();
}
for(i=0;i<num;i++)
{
for(j=0;j<num;j++)
{
if(a[i] > a[j])
{
temp = a[i];
a[i] = a[j];
a[j] = temp;
}
}
}

for(i=0;i<num;i++)
{
System.out.println(a[i]);
}
}
}
