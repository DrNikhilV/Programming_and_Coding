#include<stdio.h>
#include<ctype.h>

char Stack[100];
int top = -1;

void push(char x)
{
    Stack[++top] = x;
}

char pop()
{
    if(top == -1)
    {
        return -1;
    }
    else
    {
        return Stack[top--];
    }
}

int precedence(char x)
{
    if(x == '(')
    {
        return 0;
    }

    if (x == '+' || x == '-')
    {
        return 1;
    }

    if (x == '*' || x == '/')
    {
        return 2;
    }
}

int main()
{
    char exp[100];
    char *e;
    int x;
    printf("Enter the expression : \n");
    scanf("%s",exp);
    e = exp;

    while (*e != '\0')
    {
        if (isalnum(*e))
        {
            printf("%c ",*e);
        }

        else if (*e == '(')
        {
            push(*e);
        }

        else if (*e == ')')
        {
            while((x = pop()) != '(' )
            {
                printf("%c ",x);
            }
        }
        else
        {
            while(precedence(Stack[top]) >= precedence(*e))
            {
                printf("%c ",pop());
            }
            push(*e);
        }

        e++;
    }
    while (top != -1)
    {
        printf("%c ",pop());
    }
    return 0;
}
