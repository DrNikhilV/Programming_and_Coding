import java.io.*;

class ThreadNaming extends Thread 
{
	ThreadNaming(String name)
	{
		super(name);
	}

	@Override public void run()
	{
		System.out.println("Thread is running.....");
	}
}

class GFG {
	public static void main(String[] args)
	{
		ThreadNaming t1 = new ThreadNaming("geek1");
		ThreadNaming t2 = new ThreadNaming("geek2");

		System.out.println("Thread 1: " + t1.getName());
		System.out.println("Thread 2: " + t2.getName());

		t1.start();
		t2.start();
	}
}
