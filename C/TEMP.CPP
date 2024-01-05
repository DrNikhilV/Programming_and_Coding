#include<stdio.h>
#include<conio.h>

void asc(int a[],int n)
{
int i,j,t;
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(a[i]>a[j])
{
t=a[i];
a[i]=a[j];
a[j]=t;
}
}
}
for(i=0;i<n;i++)
{
printf("\n %d",a[i]);
}
}

void main()
{
int p[100],q[100],r[100],i,n,l=0,m=0;
clrscr();
printf("Enter n value= ");
scanf("%d",&n);
printf(" Type the array");
for(i=0;i<n;i++)
{
scanf("%d",&p[i]);
}

for(i=0;i<n;i++)
{
if ((p[i]%2)==0)
{
q[l]=p[i];
l=l+1;
}
else
{
r[m]=p[i];
m=m+1;
}
}

asc(q[],l);
asc(r[],m);
getch();
}


