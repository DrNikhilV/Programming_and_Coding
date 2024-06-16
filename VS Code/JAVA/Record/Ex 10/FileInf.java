import java.util.Scanner;
import java.io.File;
class FileInf
{
public static void main(String args[])
 {
Scanner in=new Scanner(System.in);
System.out.print("Enter file name : ");
String s=in.nextLine();
File f=new File(s);
System.out.println("FILE INFORMATION");
System.out.println("FILE NAME \t"+f.getName());
System.out.println("FILE PATH \t"+f.getPath());
System.out.println("ABSOLUTE PATH\t"+f.getAbsolutePath());
System.out.println("PARENT \t\t"+f.getParent());
System.out.println("FILE SIZE \t"+f.length()+" Bytes");
System.out.println("Is File ? \t"+f.isFile());
System.out.println("Is Directory ? \t"+f.isFile());
System.out.println("Is Readable? \t"+f.canRead());
System.out.println("Is Writable? \t"+f.canWrite());
System.out.println("Is Absolute? \t"+f.isAbsolute());
System.out.println("Is Hidden? \t"+f.isHidden());
 }
}
