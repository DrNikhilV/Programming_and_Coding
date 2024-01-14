import java.net.*;
import java.io.*;
public class EchoServer
{
 public static void main(String args[])
 {
 String str;
 try
 {
 ServerSocket ss=new ServerSocket(9000);
 Socket s=ss.accept();
 DataInputStream dis=new DataInputStream(s.getInputStream());
 PrintStream ps=new PrintStream(s.getOutputStream());
 while(true)
 {
 str=dis.readLine();
 ps.println(str);
 }
 }
 catch(IOException e)
 {
 System.out.println(e);
 }
 }
} 