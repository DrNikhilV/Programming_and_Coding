public class Main
{
public static void main(String[] args) {
try
{
int a = Integer.parseInt(args[0]);
int b = Integer.parseInt(args[1]);
System.out.println("Quotient"+ a/b);
}
catch(ArithmeticException e)
{
System.out.println("Error in denominator");
}
catch(ArrayIndexOutOfBoundsException e)
{
System.out.println("Error in index value");
}
catch(NumberFormatException e)
{
System.out.println("Data type Error");
}
finally
{
System.out.println("finally block");
}
}
}