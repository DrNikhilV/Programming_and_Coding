import java.net.*;
import java.io.*;
public class EchoClient
{
 public static void main(String arg[])
 {
 String str;
 try
 {
 InetAddress ia=InetAddress.getLocalHost();
 Socket s=new Socket(ia,9000);
 PrintStream ps=new PrintStream(s.getOutputStream());
 DataInputStream dis=new DataInputStream(System.in);
 DataInputStream dis1=new DataInputStream(s.getInputStream());
 while(true)
 {
 System.out.println("Client:");
 str=dis.readLine();
 ps.println(str);
 System.out.println("Server:"+dis1.readLine());
 }
 }
 catch(IOException e)
 {
 System.out.println(e);
 }
 }
} 