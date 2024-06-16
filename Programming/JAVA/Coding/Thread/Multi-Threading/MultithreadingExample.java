public class MultithreadingExample implements Runnable 
{

    public static void main(String[] args) 
    {
       Thread thread1 = new Thread(new MultithreadingExample());
       Thread thread2 = new Thread(new MultithreadingExample());
       thread1.start();
       thread2.start();
    }
 
    public void run() 
    {
       System.out.println("Thread running...");
    }
 }
 