// Step 1: Shape interface
public interface Shape {
    void draw();
}

// Step 2: Concrete Shape classes
public class Rectangle implements Shape {
    public void draw() {
        System.out.println("Inside Rectangle::draw() method.");
    }
}

public class Square implements Shape {
    public void draw() {
        System.out.println("Inside Square::draw() method.");
    }
}

public class Circle implements Shape {
    public void draw() {
        System.out.println("Inside Circle::draw() method.");
    }
}

// Step 3: Color interface
public interface Color {
    void fill();
}

// Step 4: Concrete Color classes
public class Red implements Color {
    public void fill() {
        System.out.println("Inside Red::fill() method.");
    }
}

public class Green implements Color {
    public void fill() {
        System.out.println("Inside Green::fill() method.");
    }
}

public class Blue implements Color {
    public void fill() {
        System.out.println("Inside Blue::fill() method.");
    }
}

// Step 5: Abstract Factory
public abstract class AbstractFactory {
    abstract Shape getShape(String shape);
    abstract Color getColor(String color);
}

// Step 6: ShapeFactory
public class ShapeFactory extends AbstractFactory {
    public Shape getShape(String shapeType) {
        if (shapeType == null) {
            return null;
        }
        if (shapeType.equalsIgnoreCase("CIRCLE")) {
            return new Circle();
        } else if (shapeType.equalsIgnoreCase("RECTANGLE")) {
            return new Rectangle();
        } else if (shapeType.equalsIgnoreCase("SQUARE")) {
            return new Square();
        }
        return null;
    }

    public Color getColor(String color) {
        return null;
    }
}

// Step 7: ColorFactory
public class ColorFactory extends AbstractFactory {
    public Shape getShape(String shape) {
        return null;
    }

    public Color getColor(String color) {
        if (color == null) {
            return null;
        }
        if (color.equalsIgnoreCase("RED")) {
            return new Red();
        } else if (color.equalsIgnoreCase("GREEN")) {
            return new Green();
        } else if (color.equalsIgnoreCase("BLUE")) {
            return new Blue();
        }
        return null;
    }
}

// Step 8: FactoryProducer
public class FactoryProducer {
    public static AbstractFactory getFactory(String choice) {
        if (choice.equalsIgnoreCase("SHAPE")) {
            return new ShapeFactory();
        } else if (choice.equalsIgnoreCase("COLOR")) {
            return new ColorFactory();
        }
        return null;
    }
}

// Step 9: Demo
public class AbstractFactoryPatternDemo {
    public static void main(String[] args) {
        // Shape Factory
        AbstractFactory shapeFactory = FactoryProducer.getFactory("SHAPE");
        Shape shape1 = shapeFactory.getShape("CIRCLE");
        shape1.draw();

        Shape shape2 = shapeFactory.getShape("RECTANGLE");
        shape2.draw();

        Shape shape3 = shapeFactory.getShape("SQUARE");
        shape3.draw();

        // Color Factory
        AbstractFactory colorFactory = FactoryProducer.getFactory("COLOR");
        Color color1 = colorFactory.getColor("RED");
        color1.fill();

        Color color2 = colorFactory.getColor("GREEN");
        color2.fill();

        Color color3 = colorFactory.getColor("BLUE");
        color3.fill();
    }
}
