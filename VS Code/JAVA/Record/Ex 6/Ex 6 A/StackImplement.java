import java.util.*;
interface StackIntf
{
boolean isEmpty();
boolean isFull();
void push(int x);
int pop();
}
class ArrayStack implements StackIntf
{
protected int arr[];
protected int top, size, len;
public ArrayStack(int n)
 {
size = n;
len = 0;
arr = new int[size];
top = -1;
 }
public boolean isEmpty()
 {
return top == -1;
 }
public boolean isFull()
 {
return top == size -1 ; 
 }
public int getSize()
 {
return len ;
 }
public int peek()
 {
if(isEmpty() )
 System.out.println("Underflow Exception");
return arr[top];
 }

public void push(int i)
 {
if(top + 1 >= size)
 System.out.println("Overflow Exception");
if(top + 1 < size )
arr[++top] = i;
len++ ;
 }
public int pop()
 {
if(isEmpty() )
System.out.println("Underflow Exception");
len-- ;
return arr[top--]; 
 } 
public void display()
 {
System.out.print("\nStack = ");
if (len == 0)
 {
System.out.print("Empty\n");
return ;
 }
for (int i = top; i >= 0; i--)
System.out.print(arr[i]+" ");
System.out.println();
 } 
}
public class StackImplement
{
public static void main(String[] args)
 {
Scanner scan = new Scanner(System.in); 
System.out.println("Stack Test\n");
System.out.println("Enter Size of Integer Stack ");
int n = scan.nextInt();
ArrayStack stk = new ArrayStack(n);
char ch;
do
{
System.out.println("\nStack Operations");
System.out.println("1. push");
System.out.println("2. pop");
System.out.println("3. peek");
System.out.println("4. check empty");
System.out.println("5. check full");
System.out.println("6. size");
int choice = scan.nextInt();

switch (choice)
{
case 1 : 
System.out.println("Enter integer element to push");
stk.push(scan.nextInt() );
break; 
case 2 : 
System.out.println("Popped Element = " + stk.pop());
break; 
case 3 : 
System.out.println("Peek Element = " + stk.peek());
break; 
case 4 : 
System.out.println("Empty status = " + stk.isEmpty());
break; 
case 5 :
System.out.println("Full status = " + stk.isFull());
break; 
case 6 : 
System.out.println("Size = " + stk.getSize());
break; 
default :
System.out.println("Wrong Entry \n ");
break;
 }

stk.display(); 
System.out.println("\nDo you want to continue (Type y or n) \n");
ch = scan.next().charAt(0);
 } while (ch == 'Y'|| ch == 'y'); 
 }
}