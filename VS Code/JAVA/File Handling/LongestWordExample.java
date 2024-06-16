import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class LongestWordExample {
    public static void main(String[] args) {
        String filePath = "file.txt";

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            String longestWord = "";

            while ((line = br.readLine()) != null) {
                String[] words = line.split("\\s+");

                for (String word : words) {
                    if (word.length() > longestWord.length()) {
                        longestWord = word;
                    }
                }
            }

            System.out.println("Longest word: " + longestWord);
        } catch (IOException e) {
            System.out.println("An error occurred while reading the file.");
            e.printStackTrace();
        }
    }
}