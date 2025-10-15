// A. Method Overriding
class Human {
    void eat() {
        System.out.println("Human is eating");
    }
}

class Boy extends Human {
    @Override
    void eat() {
        System.out.println("Boy is eating");
    }

    public static void main(String[] args) {
        Boy obj = new Boy();
        obj.eat(); // Calls overridden method
    }
}

// B. Interface
interface Printable {
    void print();
}

class A6 implements Printable {
    public void print() {
        System.out.println("Hello");
    }

    public static void main(String[] args) {
        A6 obj = new A6();
        obj.print();
    }
}

// C. Abstract Class
abstract class Bike {
    abstract void run();
}

class Honda4 extends Bike {
    void run() {
        System.out.println("running safely..");
    }

    public static void main(String[] args) {
        Bike obj = new Honda4();
        obj.run();
    }
}
