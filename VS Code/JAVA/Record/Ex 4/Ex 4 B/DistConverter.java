import java.io.*;
import java.util.Scanner;
public class DistConverter
{
public static void main(String args[])
 {
 Scanner in=new Scanner(System.in); 
float k = 0; 
double miles;
System.out.print("Enter the number of kilometers you wish to be converted to miles : ");
 k=in.nextInt();
miles=k * 0.621371192; 
System.out.println("Miles : "+miles+" Miles");
 }
}