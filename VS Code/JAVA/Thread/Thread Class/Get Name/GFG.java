import java.io.*;

class ThreadNaming extends Thread 
{
	@Override public void run()
	{
		System.out.println("Current thread name..");
		System.out.println(Thread.currentThread().getName());
	}
}

class GFG 
{
	public static void main(String[] args)
	{

		ThreadNaming t1 = new ThreadNaming();
		ThreadNaming t2 = new ThreadNaming();
		t1.start();
		t2.start();
	}
}
