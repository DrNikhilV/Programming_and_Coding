import java.io.*;
import java.util.Scanner;
public class CurrencyConverter
{
public static double yen,inr,euro,Y,I,E;
CurrencyConverter()
{
yen=112.212;
inr=67;
euro=87.98;
}
public static void main(String args[])
 {
CurrencyConverter C=new CurrencyConverter();
Scanner in=new Scanner(System.in); 
int dollar = 0; 
System.out.print("Enter the dollars : ");
dollar=in.nextInt();
 Y=dollar*yen;
I=dollar*inr;
E=dollar*euro;
System.out.println("YEN : "+Y+" Yen");
System.out.println("INR : "+I+" INR");
System.out.println("EURO : "+E+" Euro");
 }
}
