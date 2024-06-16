import java.io.FileWriter;
import java.io.IOException;

public class FileWritingExample {
    public static void main(String[] args) {
        FileWriter writer = null;
        try {
  
            String filePath = "file.txt";
  
            writer = new FileWriter(filePath);
            
            writer.write("Hello, World!");
            
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (writer != null) {
                    writer.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
