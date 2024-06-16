import java.lang.Exception;
class MyException extends Exception
{
MyException(String message)
{
    super(message);
}
}
class TestMyException
{
public static void main(String[] args) 
{
int x=5,y=10;
try
{
float z = (float) x / (float) y;
if(z<5.0)
{
    throw new MyException("Wrong Numbers input");
}
}
catch(MyException e)
{
System.out.println("Caught my exception");
System.out.println(e.getMessage());
}
finally
{
System.out.println("Hi! By default finally block executed");   
}
}
}

