// Step 1: Singleton Class
public class SingleObject {
    // create an object of SingleObject
    private static SingleObject instance = new SingleObject();

    // make the constructor private so that this class cannot be instantiated
    private SingleObject() {}

    // Get the only object available
    public static SingleObject getInstance() {
        return instance;
    }

    public void showMessage() {
        System.out.println("Hello World!");
    }
}

// Step 2: Demo class
public class SingletonPatternDemo {
    public static void main(String[] args) {
        // illegal construct
        // SingleObject object = new SingleObject(); // Compile-time error

        // Get the only object available
        SingleObject object = SingleObject.getInstance();

        // Show message
        object.showMessage();
    }
}
