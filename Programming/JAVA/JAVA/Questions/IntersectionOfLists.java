import java.util.ArrayList;
import java.util.List;

public class IntersectionOfLists {
    public static void main(String[] args) {
        List<Integer> list1 = new ArrayList<>();
        list1.add(1);
        list1.add(2);
        list1.add(3);
        list1.add(4);

        List<Integer> list2 = new ArrayList<>();
        list2.add(3);
        list2.add(4);
        list2.add(5);
        list2.add(6);

        List<Integer> intersection = new ArrayList<>();

        for (Integer num : list1) {
            if (list2.contains(num)) {
                intersection.add(num);
            }
        }

        System.out.println("List 1: " + list1);
        System.out.println("List 2: " + list2);
        System.out.println("Intersection: " + intersection);
    }
}