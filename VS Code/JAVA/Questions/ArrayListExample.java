import java.util.ArrayList;

public class ArrayListExample {
    public static void main(String[] args) {

        ArrayList<Integer> arrayList = new ArrayList<>();

        arrayList.add(5);
        arrayList.add(10);
        arrayList.add(15);
        arrayList.add(20);
        arrayList.add(25);

        System.out.println("ArrayList: " + arrayList);

        int size = arrayList.size();
        System.out.println("Size of ArrayList: " + size);

        int elementAtIndex2 = arrayList.get(2);
        System.out.println("Element at index 2: " + elementAtIndex2);

        boolean contains15 = arrayList.contains(15);
        System.out.println("ArrayList contains 15: " + contains15);

        arrayList.add(1, 30);
        System.out.println("ArrayList after adding 30: " + arrayList);

        boolean removed = arrayList.remove(Integer.valueOf(10));
        System.out.println("ArrayList after removing 10: " + arrayList);

        System.out.print("Elements in ArrayList: ");
        for (int element : arrayList) {
            System.out.print(element + " ");
        }
        System.out.println();

        arrayList.clear();
        System.out.println("ArrayList after clearing: " + arrayList);
    }
}