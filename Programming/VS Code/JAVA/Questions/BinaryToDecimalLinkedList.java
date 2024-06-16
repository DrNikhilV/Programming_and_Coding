import java.util.LinkedList;

public class BinaryToDecimalLinkedList {
    public static void main(String[] args) {
        LinkedList<Integer> binaryDigits = new LinkedList<>();

        binaryDigits.add(1);
        binaryDigits.add(0);
        binaryDigits.add(1);
        binaryDigits.add(0);

        int decimal = convertBinaryToDecimal(binaryDigits);

        System.out.println("Binary: " + binaryDigits);
        System.out.println("Decimal: " + decimal);
    }

    public static int convertBinaryToDecimal(LinkedList<Integer> binaryDigits) {
        int decimal = 0;
        int power = 0;

        while (!binaryDigits.isEmpty()) {
            int digit = binaryDigits.removeLast();
            decimal += digit * Math.pow(2, power);
            power++;
        }

        return decimal;
    }
}

