class Orange {
    int p,q;
    Orange(int k , int l)
    {
        p = k;
        q = l;
    }

    int display()
    {
        return p*q;
    }
        public static void main(String args[]) 
        {
            Orange ap =  new Orange(55,67);
            System.out.println("Value of p*q is " +ap.display());
        }
}
