import java.io.*;
import java.util.*;
class Max
{
public static <E extends Comparable<E>>E maximum(E[] list)
 {
 E m=list[0];
for(int i=1;i<list.length;i++)
 {
if(list[i].compareTo(m)>0)
 {
 m=list[i];
 }
 }
return m;
 }
}
class GenericTest
{
public static void main(String args[])
 {
 Integer a[]={20,10,40,30,50,70,60,90,80,};
System.out.println("Integer max : "+Max.maximum(a));
 Double b[]={20.2,10.3,4.2,3.7,1.5,5.7,67.2,23.2,80.5,};
System.out.println("Double max : "+Max.maximum(b));
 }
}
