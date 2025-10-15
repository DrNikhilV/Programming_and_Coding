class Honda4 extends Bike
{
    // Must be public to match or widen the access of the overridden abstract method
    public void run() { 
        System.out.println("running safely..");
    }

    public static void main(String[] args) {
        // Demonstrates Polymorphism
        Bike obj = new Honda4();
        obj.run();
    }
}