import java.util.*;
class StackExcep
{
static int a[],size,top;
static int choice;
StackExcep(int x)
{
a=new int[x];
size=x;
top=-1;
}
public void push(int x)throws ArithmeticException
{
try
{
if(top<4)
a[++top]=x; 
else throw new ArithmeticException();
} 
catch(ArithmeticException e)
{System.out.println("OVERFLOW STACK FULL "+Arrays.toString(a));}
}
public int pop()throws ArithmeticException
{
try
{
if(top>=0)
return(a[top--]);
else throw new ArithmeticException ();
}
catch(ArithmeticException b)
{
System.out.println("Exeption raised UNDERFLOW - STACK EMPTY - "+b);
}
return -1;
}
public void peek()
{
for(int i=0;i<=top;i++)
System.out.print(a[i]+" ");
}
public static void main(String a[])
{
StackExcep S=new StackExcep(5);
Scanner in=new Scanner(System.in);
do
{
System.out.println();
System.out.println("1.PUSH");
System.out.println("2.POP");
System.out.println("3.PEEK");
System.out.println("4.EXIT");
choice=in.nextInt();
switch(choice)
{

case 1:
System.out.print("Give the item to be pushed : ");
int data;
data=in.nextInt();
S.push(data);
break;
case 2:
System.out.print("POP : "+S.pop());
break;
case 3:
System.out.println("PEEK CONTENTS : ");
S.peek();
break;
}
 }
while(choice<4);
 }
}
