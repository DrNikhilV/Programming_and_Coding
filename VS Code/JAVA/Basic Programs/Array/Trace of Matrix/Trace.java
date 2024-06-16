import java.util.*;
class Trace
{
public static void main(String args[])
{
int num;
System.out.println("Enter size of array : ");
Scanner sr = new Scanner(System.in);
num = sr.nextInt();
int a[][] = new int[num][num];

int i,j,temp=0;
System.out.println("Enter the array : ");

for(i=0;i<num;i++)
{
for(j=0;j<num;j++)
{
a[i][j] = sr.nextInt();
}
}


for(i=0;i<num;i++)
{
for(j=0;j<num;j++)
{
if(i == j)
{
temp = temp + a[i][j];
}
}
}

System.out.println(temp);
}
}
