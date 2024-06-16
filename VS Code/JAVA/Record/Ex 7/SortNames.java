import java.io.*;
import java.util.*;
class SortNames
{
public static void main(String args[]) throws Exception 
{
int n,i;
String str;
Scanner in=new Scanner(System.in);
ArrayList names=new ArrayList();
System.out.println("Enter the number of names : ");
n=in.nextInt();
str=in.nextLine();
for(i=0;i<n;i++)
{
System.out.println("Enter name "+(i+1)+ ": ");
str=in.nextLine();
names.add(new String(str));
}
System.out.println("Unsorted ArrayList is : "+names);
Collections.sort(names);
System.out.println("Sorted ArrayList is : "+names);
}
}
