import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class AverageNumberExample {
    public static void main(String[] args) {
        String filePath = "num.txt";

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            int sum = 0;
            int count = 0;

            while ((line = br.readLine()) != null) {
                int number = Integer.parseInt(line);
                sum += number;
                count++;
            }

            double average = (double) sum / count;

            System.out.println("Average: " + average);
        } catch (IOException e) {
            System.out.println("An error occurred while reading the file.");
            e.printStackTrace();
        }
    }
}
