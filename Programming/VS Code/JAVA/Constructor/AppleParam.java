 class AppleParam 
{
    static int x;
    AppleParam(int k)
    {
        x = k;
    }
    public static void main(String[] args) {
        new AppleParam(5);
        System.out.println("Value of variable is : "+x);
    }
}
