import java.util.Stack;

public class PalindromeCheck {
    public static boolean isPalindrome(String input) {
        Stack<Character> stack = new Stack<>();
        StringBuilder reversed = new StringBuilder();

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            stack.push(c);
        }

        while (!stack.isEmpty()) {
            char c = stack.pop();
            reversed.append(c);
        }

        return input.equals(reversed.toString());
    }

    public static void main(String[] args) {
        String input1 = "radar";
        String input2 = "hello";

        System.out.println("Is '" + input1 + "' a palindrome? " + isPalindrome(input1));
        System.out.println("Is '" + input2 + "' a palindrome? " + isPalindrome(input2));
    }
}