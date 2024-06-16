import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
public class FileReadingExample2 {
    public static void main(String[] args) {
        String filePath = "file.txt";
        File file = new File(filePath);
        
        try {
    
            Scanner scanner = new Scanner(file);
       
            StringBuilder content = new StringBuilder();
            while (scanner.hasNextLine()) {
                content.append(scanner.nextLine()).append("\n");
            }
            
            scanner.close();
            
            System.out.println("File Content:\n" + content.toString());
            
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
