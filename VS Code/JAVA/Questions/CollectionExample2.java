import java.util.*;

public class CollectionExample2 {
    public static void main(String[] args) {
        List<String> words = Arrays.asList("apple", "banana", "apple", "orange", "banana", "apple", "grape");

        Map<String, Integer> frequencyMap = new HashMap<>();
        for (String word : words) {
            if (frequencyMap.containsKey(word)) {
                frequencyMap.put(word, frequencyMap.get(word) + 1);
            } else {
                frequencyMap.put(word, 1);
            }
        }
        int maxFrequency = 0;
        for (int frequency : frequencyMap.values()) {
            maxFrequency = Math.max(maxFrequency, frequency);
        }

        List<String> mostFrequentWords = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : frequencyMap.entrySet()) {
            if (entry.getValue() == maxFrequency) {
                mostFrequentWords.add(entry.getKey());
            }
        }

        System.out.println("Most frequent word(s):");
        for (String word : mostFrequentWords) {
            System.out.println(word);
        }
    }
}