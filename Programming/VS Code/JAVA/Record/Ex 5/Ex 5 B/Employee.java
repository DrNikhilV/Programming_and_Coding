import java.io.*;
class Employee
{
static String name;
static int id;
static int deptc;
static String add;
Employee(String a,int b, String c,int d)
{
name=a;id=b;
add=c;
deptc=d;
}
}
class Programmer extends Employee
{
static double bp;
static double allowance,ded,da,hra,pf,sc , netsalary;
Programmer(String a,int b,String c,int d,double x)
{
super(a,b,c,d);
bp=x;
}
public static void printpayslip()
{
da=0.97*bp;
hra=0.10*bp;
pf=0.12*bp;
sc=0.01*bp;
ded=pf+sc;
allowance=hra+da;
netsalary=bp+allowance-ded;
System.out.println("---------------------------------------");
System.out.println(" ARISE COMPANY LIMITED ");
System.out.println("---------------------------------------");
System.out.print("Name:"+name);
System.out.println(" Emp.Id:"+id);
System.out.print("Address:"+add);
System.out.println(" Dept.code:"+deptc);
System.out.println("General Details");
System.out.println("----------");
System.out.print("Deduction:"+ded);
System.out.println("\tAllowance:"+allowance);
System.out.println("---------------------------------------");
System.out.println("Salary of " +name);
System.out.println("Netsalary:"+netsalary);
System.out.println("Good Job");
System.out.println("---------------------------------------");
}
}

classAssistProf extends Employee
{
static double bp;
static double allowance,ded,da,hra,pf,sc,netsalary;
AssistProf(String a,int b,String c,int d,double x)
{
super(a,b,c,d);
bp=x;
}
public static void printpayslip()
{
da=0.97*bp;
hra=0.10*bp;
pf=0.12*bp;
sc=0.01*bp;
ded=pf+sc;
allowance=hra+da;
netsalary=bp+allowance-ded;
System.out.println("---------------------------------------");
System.out.println(" KR Group of Institutions ");
System.out.println("---------------------------------------");
System.out.print("Name:"+name);
System.out.println(" Emp.Id:"+id);
System.out.print("Address:"+add);
System.out.println(" Dept.code:"+deptc);
System.out.println("General Details");
System.out.println("----------------------------------------");
System.out.print("Deduction:"+ded);
System.out.println("\tAllowance:"+allowance);
System.out.println("---------------------------------------");
System.out.println("Salary of " +name);
System.out.println("Netsalary:"+netsalary);
System.out.println("Good Job");
System.out.println("---------------------------------------");
}
}
classAssocProf extends Employee
{
static double bp;
static double allowance,ded,da,hra,pf,sc,netsalary;
AssocProf(String a,int b,String c,int d,double x)
{
super(a,b,c,d);
bp=x;
}
public static void printpayslip()
{
da=0.97*bp;
hra=0.10*bp;
pf=0.12*bp;
sc=0.01*bp;
ded=pf+sc;
allowance=hra+da;
netsalary=bp+allowance-ded;
System.out.println("---------------------------------------");
System.out.println(" KR Group of Institutions ");
System.out.println("---------------------------------------");
System.out.print("Name:"+name);
System.out.println(" Emp.Id:"+id);
System.out.print("Address:"+add);
System.out.println(" Dept.code:"+deptc);
System.out.println("General Details");
System.out.println("----------------------------------------");
System.out.print("Deduction:"+ded);
System.out.println("\tAllowance:"+allowance);
System.out.println("---------------------------------------");
System.out.println("Salary of " +name);
System.out.println("Netsalary:"+netsalary);
System.out.println("Good Job");
System.out.println("---------------------------------------");
}
}
class Prof extends Employee
{
static double bp;
static double allowance,ded,da,hra,pf,sc,netsalary;
Prof(String a,int b,String c,int d,double x)
{
super(a,b,c,d);
bp=x;
}
public static void printpayslip()
{
da=0.97*bp;
hra=0.10*bp;
pf=0.12*bp;
sc=0.01*bp;
ded=pf+sc;
allowance=hra+da;
netsalary=bp+allowance-ded;
System.out.println("---------------------------------------");
System.out.println(" KR Group of Institutions ");
System.out.println("---------------------------------------");
System.out.print("Name:"+name);
System.out.println(" Emp.Id:"+id);
System.out.print("Address:"+add);
System.out.println(" Dept.code:"+deptc);
System.out.println("General Details");
System.out.println("----------------------------------------");
System.out.print("Deduction:"+ded);
System.out.println("\tAllowance:"+allowance);

System.out.println("---------------------------------------");
System.out.println("Salary of " +name);
System.out.println("Netsalary:"+netsalary);
System.out.println("Good Job");
System.out.println("---------------------------------------");
}
}
class EmployeePay
{
public static void main(String args[])
{
Programmer p1=new Programmer("Raja",01,"Trichy",78,5000);
p1.printpayslip();
AssistProf p2=new AssistProf("Haritha",02,"Chennai",78,1000);
p2.printpayslip();
AssocProf p3=new AssocProf("Jeeva",03,"Madurai",78,20000);
p3.printpayslip();
Prof p4=new Prof("Raagul",04,"Trichy",78,30000);
p4.printpayslip();
}
}
