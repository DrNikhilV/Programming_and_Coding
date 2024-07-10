#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

struct Node* insertNode(struct Node* root, int data) {
    if (root == NULL) {
        return createNode(data);
    }
    if (data < root->data) {
        root->left = insertNode(root->left, data);
    } else if (data > root->data) {
        root->right = insertNode(root->right, data);
    }
    return root;
}

void preOrderTraversal(struct Node* root) {
    if (root == NULL) {
        return;
    }
    printf("%d ", root->data);
    preOrderTraversal(root->left);
    preOrderTraversal(root->right);
}

int main() {
    struct Node* root = NULL;
    int n;
    printf("Enter the number of elements in the tree: ");
    scanf("%d", &n);

    printf("Enter the elements of the tree:\n");
    for (int i = 0; i < n; i++) {
        int data;
        scanf("%d", &data);
        root = insertNode(root, data);
    }

    printf("Pre-Order Traversal: ");
    preOrderTraversal(root);
    printf("\n");

    return 0;
}
