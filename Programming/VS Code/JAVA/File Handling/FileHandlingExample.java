import java.io.FileWriter;
import java.io.IOException;

public class FileHandlingExample {
    public static void main(String[] args) {
        try (FileWriter writer = new FileWriter("file.txt", true)) {
            writer.write("This is additional content.");
            writer.write(" It will be appended to the file.");
            System.out.println("Content appended to the file.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
