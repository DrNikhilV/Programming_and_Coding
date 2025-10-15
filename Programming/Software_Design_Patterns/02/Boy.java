class Boy extends Human
{
    @Override
    void eat() {
        System.out.println("Boy is eating");
    }

    public static void main(String[] args) {
        Boy obj = new Boy();
        obj.eat(); // Calls overridden method
    }
}