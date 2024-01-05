#include<stdio.h>
#include<conio.h>
void main()
{
char a[50];
clrscr();
FILE*f;
f=fopen("Rich Text Format.rtf","a");
fprintf(f,"Hello, How are you?  ");
fclose(f);
clrscr();
f=fopen("Rich Text Format.rtf","r");
while (fscanf(f,"%s",a)!=EOF)
{
printf("%s",a);
}
fclose(f);
getch();
}
