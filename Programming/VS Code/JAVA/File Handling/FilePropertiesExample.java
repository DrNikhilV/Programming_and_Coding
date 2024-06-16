import java.io.File;
import java.util.Date;

public class FilePropertiesExample {
    public static void main(String[] args) {
        File file = new File("file.txt");

        long fileSize = file.length();
        System.out.println("File size: " + fileSize + " bytes.");

        long lastModified = file.lastModified();
        Date lastModifiedDate = new Date(lastModified);
        System.out.println("Last modified: " + lastModifiedDate);

        if (file.isFile()) {
            System.out.println("It is a file.");
        } else if (file.isDirectory()) {
            System.out.println("It is a directory.");
        }
        if (file.exists()) {
            System.out.println("File exists.");
        } else {
            System.out.println("File does not exist.");
        }
    }
}

