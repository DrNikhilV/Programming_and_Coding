import java.util.Scanner;

public class Wifi
{
	public static void main(String args[])
	{
		Scanner sr = new Scanner(System.in);
		System.out.println("Enter name : ");
		String name = sr.nextLine();
		System.out.println("Enter room Number : ");
		int n = sr.nextInt();
		System.out.println("Wifi pwd: " + name.substring(0, 2) + n + "$@"); 
		sr.close();
	}
}