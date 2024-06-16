import java.util.*;

public class CollectionExample {
    public static void main(String[] args) {
        Map<String, Integer> studentGrades = new HashMap<>();
        studentGrades.put("Alice", 85);
        studentGrades.put("Bob", 92);
        studentGrades.put("Charlie", 78);
        studentGrades.put("David", 95);
        studentGrades.put("Eva", 88);


        String highestGradeStudent = "";
        int highestGrade = Integer.MIN_VALUE;
        for (Map.Entry<String, Integer> entry : studentGrades.entrySet()) {
            if (entry.getValue() > highestGrade) {
                highestGrade = entry.getValue();
                highestGradeStudent = entry.getKey();
            }
        }

        System.out.println("Student with the highest grade: " + highestGradeStudent);
    }
} 

