package Multiplication;
class Multithread extends Thread 
{
	public void run()
	{
		try 
		{
			System.out.print(" Thread " + Thread.currentThread().getId()+ " ");
		}

		catch (Exception e) 
		{
			System.out.println("Exception is caught");
		}
	}
}

public class Multiply
{
	public static void main(String[] args)
	{
		int n = 2;
		for (int i = 1; i <=10 ; i++) 
		{
            Multithread object = new Multithread();
            System.out.println(i +" * "+n+" = "+i*n);
			object.start();
		}
	}
}
