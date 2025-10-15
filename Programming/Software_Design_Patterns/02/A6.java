class A6 implements Printable
{
    // Must be public to implement the interface method
    public void print() {
        System.out.println("Hello");
    }

    public static void main(String[] args) {
        A6 obj = new A6();
        obj.print();
    }
}