#include <stdio.h>
#define SIZE 100

struct TreeNode 
{
    int data;
    int isEmpty;
};

void initialize(struct TreeNode tree[], int n) 
{
    int i;
    for (i = 0; i < n; i++) 
    {
        tree[i].isEmpty = 1;
    }
}

void insert(struct TreeNode tree[], int n, int value) 
{
    int i;
    for (i = 0; i < n; i++) 
    {
        if (tree[i].isEmpty == 1) 
        {
            tree[i].data = value;
            tree[i].isEmpty = 0;
            break;
        }
    }
}

void display(struct TreeNode tree[], int n) 
{
    int i;
    printf("Binary Tree: ");
    for (i = 0; i < n; i++) 
    {
        if (tree[i].isEmpty == 0) 
        {
            printf("%d ", tree[i].data);
        }
    }
    printf("\n");
}

int main() 
{
    struct TreeNode tree[SIZE];
    int n = SIZE;
    int value, numNodes, i;

    initialize(tree, n);

    printf("Enter the number of nodes to insert: ");
    scanf("%d", &numNodes);

    printf("Enter the values to insert:\n");
    for (i = 0; i < numNodes; i++) 
    {
        scanf("%d", &value);
        insert(tree, n, value);
    }

    display(tree, n);

    return 0;
}
