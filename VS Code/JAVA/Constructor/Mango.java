public class Mango {
    int p,q;
    Mango(int k, int l)
    {
        p=k;
        q=l;
    }
    int display()
    {
        return p*q;
    }
    public static void main(String[] args) {
        Orange ap = new Orange(10,20);
        int ab = ap.display();
        System.out.println("Value of p*q = "+ab);
    }
}
