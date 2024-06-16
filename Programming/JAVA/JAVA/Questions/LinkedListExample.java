import java.util.LinkedList;

public class LinkedListExample {
    public static void main(String[] args) {

        LinkedList<String> linkedList = new LinkedList<>();

        linkedList.add("Apple");
        linkedList.add("Banana");
        linkedList.add("Cherry");
        linkedList.add("Durian");

        System.out.println("LinkedList: " + linkedList);

        int size = linkedList.size();
        System.out.println("Size of LinkedList: " + size);

        String firstElement = linkedList.get(0);
        System.out.println("First element: " + firstElement);

        boolean containsDurian = linkedList.contains("Durian");
        System.out.println("LinkedList contains Durian: " + containsDurian);

        linkedList.add(2, "Grapes");
        System.out.println("LinkedList after adding Grapes: " + linkedList);

        boolean removed = linkedList.remove("Cherry");
        System.out.println("LinkedList after removing Cherry: " + linkedList);

        System.out.print("Elements in LinkedList: ");
        for (String element : linkedList) {
            System.out.print(element + " ");
        }
        System.out.println();

        linkedList.clear();
        System.out.println("LinkedList after clearing: " + linkedList);
    }
}