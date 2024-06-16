class A extends Thread
{
public void run()
  {
  System.out.println("thread-A Started");
  for(int i=1;i<=4;i++)
  {
      System.out.println("From thread-A :"+i+"\n");
  }
  System.out.println("Exit from A");   
  }
}

class B extends Thread
{
public void run()
  {
  System.out.println("thread-B Started\n");
  for(int j=1;j<=4;j++)
  {
      System.out.println("From thread-B :"+j+"\n");
  }
  System.out.println("Exit from B\n");  
  }
}

class C extends Thread
{
public void run()
  {
  System.out.println("thread-C Started\n");
  for(int k=1;k<=4;k++)
  {
      System.out.println("From thread-C :"+k+"\n");
  }
  System.out.println("Exit from C\n");   
  }
}

class ThreadPriority 
{
    public static void main(String[] args) 
    {
        A threadA = new A();
        B threadB = new B();
        C threadC = new C();
        
        threadC.setPriority(Thread.MAX_PRIORITY);
        threadB.setPriority(threadA.getPriority()+1);
        threadA.setPriority(Thread.MIN_PRIORITY);
        System.out.println("Start thread A\n");
        threadA.start();
        System.out.println("Start thread B\n");
        threadB.start();
        System.out.println("Start thread C\n");
        threadC.start();
        System.out.println("End of main thread");
}
}