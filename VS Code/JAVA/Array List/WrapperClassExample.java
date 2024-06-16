public class WrapperClassExample {
    public static void main(String[] args) {
        int num = 10;
        Integer wrappedNum = Integer.valueOf(num);
        System.out.println("Wrapped number: " + wrappedNum);
        
        boolean bool = true;
        Boolean wrappedBool = Boolean.valueOf(bool);
        System.out.println("Wrapped boolean: " + wrappedBool);
        
        char ch = 'a';
        Character wrappedChar = Character.valueOf(ch);
        System.out.println("Wrapped character: " + wrappedChar);
        
        double dbl = 3.14159;
        Double wrappedDbl = Double.valueOf(dbl);
        System.out.println("Wrapped double: " + wrappedDbl);
    }
}
