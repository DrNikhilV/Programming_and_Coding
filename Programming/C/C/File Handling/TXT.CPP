#include<stdio.h>
#include<conio.h>
void main()
{
char a[50];
clrscr();
FILE*f;
f=fopen("Text.txt","a");
fprintf(f,"Hello  ");
fclose(f);
clrscr();
f=fopen("Text.txt","r");
while (fscanf(f,"%s",a)!=EOF)
{
printf("%s",a);
}
fclose(f);
getch();
}
