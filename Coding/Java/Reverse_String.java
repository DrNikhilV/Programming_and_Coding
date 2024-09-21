public class ReverseString {

    public static void main(String[] args) {
        String name = "Nikhil";
        
        // 1. Using StringBuilder
        System.out.println(new StringBuilder(name).reverse().toString());
        
        // 2. Reverse using one pointer
        String revName = "";
        for (int i = name.length() - 1; i >= 0; i--) {
            revName += name.charAt(i);
        }
        System.out.println(revName);

        // 3. Two pointers (in-place reverse)
        char[] nameArray = name.toCharArray();
        int left = 0;
        int right = nameArray.length - 1;

        while (left < right) {
            char temp = nameArray[left];
            nameArray[left] = nameArray[right];
            nameArray[right] = temp;
            left++;
            right--;
        }

        String reversedInPlace = new String(nameArray);
        System.out.println("Reversed with two pointers (in-place): " + reversedInPlace);
    }
}
