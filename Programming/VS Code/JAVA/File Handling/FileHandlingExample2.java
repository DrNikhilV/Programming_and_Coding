import java.io.File;
import java.io.IOException;
  
public class FileHandlingExample2 {
    public static void main(String[] args) {

        File directory = new File("mydir");
        if (!directory.exists()) {
            if (directory.mkdir()) {
                System.out.println("Directory created successfully.");
            } else {
                System.out.println("Failed to create the directory.");
            }
        }
  
        File file = new File("mydir/myfile.txt");
        try {
            if (file.createNewFile()) {
                System.out.println("File created successfully.");
            } else {
                System.out.println("Failed to create the file.");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        if (file.delete()) {
            System.out.println("File deleted successfully.");
        } else {
            System.out.println("Failed to delete the file.");
        }
  
        if (directory.delete()) {
            System.out.println("Directory deleted successfully.");
        } else {
            System.out.println("Failed to delete the directory.");
        }
    }
}

