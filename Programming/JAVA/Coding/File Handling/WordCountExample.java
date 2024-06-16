import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class WordCountExample {
    public static void main(String[] args) {
        String filePath = "file.txt";

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            int wordCount = 0;

            while ((line = br.readLine()) != null) {
                String[] words = line.split("\\s+");
                wordCount += words.length;
            }

            System.out.println("Total number of words: " + wordCount);
        } catch (IOException e) {
            System.out.println("An error occurred while reading the file.");
            e.printStackTrace();
        }
    }
}