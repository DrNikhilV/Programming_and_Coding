import java.util.LinkedList;
import java.util.Queue;

public class QueueExample {
    public static void main(String[] args) {
  
        Queue<String> queue = new LinkedList<>();

        queue.offer("Apple");
        queue.offer("Banana");
        queue.offer("Cherry");
        queue.offer("Durian");

        System.out.println("Queue: " + queue);

        int size = queue.size();
        System.out.println("Size of Queue: " + size);

        String frontElement = queue.peek();
        System.out.println("Front element: " + frontElement);

        boolean isEmpty = queue.isEmpty();
        System.out.println("Queue is empty: " + isEmpty);

        String dequeuedElement = queue.poll();
        System.out.println("Dequeued element: " + dequeuedElement);

        queue.offer("Grapes");
        System.out.println("Queue after enqueuing Grapes: " + queue);

        System.out.print("Elements in Queue: ");
        for (String element : queue) {
            System.out.print(element + " ");
        }
        System.out.println();

        queue.clear();
        System.out.println("Queue after clearing: " + queue);
    }
}