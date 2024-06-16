import java.io.*;
import java.net.*;
class PingTest{
    public static void main(String[] args) {
        try{
            Runtime r = Runtime.getRuntime();
            Process p =r.exec("ping 127.0.0.1");
            BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String inputLine;
            while((inputLine = in.readLine())!=null)
            {
                System.out.println(inputLine);
            }
            in.close();
            }
        catch(IOException e){
            System.out.println(e);
        }
    }
}