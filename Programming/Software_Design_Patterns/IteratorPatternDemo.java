// Step 1: Create interfaces
public interface Iterator {
    public boolean hasNext();
    public Object next();
}

public interface Container {
    public Iterator getIterator();
}

// Step 2: Create concrete class implementing Container interface
public class NameRepository implements Container {
    public String names[] = {"Robert", "John", "Julie", "Lora"};

    @Override
    public Iterator getIterator() {
        return new NameIterator();
    }

    private class NameIterator implements Iterator {
        int index;

        @Override
        public boolean hasNext() {
            return index < names.length;
        }

        @Override
        public Object next() {
            if(this.hasNext()) {
                return names[index++];
            }
            return null;
        }
    }
}

// Step 3: Demo class
public class IteratorPatternDemo {
    public static void main(String[] args) {
        NameRepository namesRepository = new NameRepository();

        for(Iterator iter = namesRepository.getIterator(); iter.hasNext();) {
            String name = (String) iter.next();
            System.out.println("Name : " + name);
        }
    }
}
