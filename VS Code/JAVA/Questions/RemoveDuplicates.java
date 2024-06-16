import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class RemoveDuplicates {
    public static void main(String[] args) {
        List<String> originalList = new ArrayList<>();
        originalList.add("Apple");
        originalList.add("Banana");
        originalList.add("Mango");
        originalList.add("Banana");
        originalList.add("Orange");
        originalList.add("Apple");

        List<String> uniqueList = new ArrayList<>(new HashSet<>(originalList));

        System.out.println("Original List: " + originalList);
        System.out.println("List without Duplicates: " + uniqueList);
    }
}