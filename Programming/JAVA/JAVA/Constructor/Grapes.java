public class Grapes {
    int x,y,z;
    Grapes(int a,int b,int c)
    {
        x=a;
        y=b;
        z=c;
    }

    int display()
    {
        return x*y*z;
    }

    public static void main(String[] args) 
    {
        Grapes gr = new Grapes(1,2,3);
        System.out.println("The value of a*b*c = "+gr.display());
    }
}
