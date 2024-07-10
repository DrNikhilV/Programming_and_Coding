#include <stdio.h>
#include <stdlib.h>

struct AVLNode {
    int data;
    struct AVLNode* left;
    struct AVLNode* right;
    int height;
};
struct AVLNode* createNode(int value) {
    struct AVLNode* newNode = (struct AVLNode*)malloc(sizeof(struct AVLNode));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    newNode->height = 1;
    return newNode;
}
int getHeight(struct AVLNode* node) {
    if (node == NULL) {
        return 0;
    }
    return node->height;
}

void updateHeight(struct AVLNode* node) {
    int leftHeight = getHeight(node->left);
    int rightHeight = getHeight(node->right);
    node->height = (leftHeight > rightHeight ? leftHeight : rightHeight) + 1;
}
struct AVLNode* rotateRight(struct AVLNode* node) {
    struct AVLNode* newRoot = node->left;
    struct AVLNode* temp = newRoot->right;

    newRoot->right = node;
    node->left = temp;

    updateHeight(node);
    updateHeight(newRoot);

    return newRoot;
}

struct AVLNode* rotateLeft(struct AVLNode* node) {
    struct AVLNode* newRoot = node->right;
    struct AVLNode* temp = newRoot->left;

    newRoot->left = node;
    node->right = temp;

    updateHeight(node);
    updateHeight(newRoot);

    return newRoot;
}

struct AVLNode* balanceNode(struct AVLNode* node) {
    updateHeight(node);

    int balanceFactor = getHeight(node->left) - getHeight(node->right);

    if (balanceFactor > 1 && getHeight(node->left->left) >= getHeight(node->left->right)) {
        return rotateRight(node);
    }

    if (balanceFactor < -1 && getHeight(node->right->right) >= getHeight(node->right->left)) {
        return rotateLeft(node);
    }

    if (balanceFactor > 1 && getHeight(node->left->left) < getHeight(node->left->right)) {
        node->left = rotateLeft(node->left);
        return rotateRight(node);
    }

    if (balanceFactor < -1 && getHeight(node->right->right) < getHeight(node->right->left)) {
        node->right = rotateRight(node->right);
        return rotateLeft(node);
    }

    return node;
}

struct AVLNode* findMinNode(struct AVLNode* node) {
    struct AVLNode* current = node;
    while (current && current->left != NULL) {
        current = current->left;
    }
    return current;
}

struct AVLNode* deleteNode(struct AVLNode* root, int value) {
    if (root == NULL) {
        return root;
    }

    if (value < root->data) {
        root->left = deleteNode(root->left, value);
    } else if (value > root->data) {
        root->right = deleteNode(root->right, value);
    } else {
        if (root->left == NULL || root->right == NULL) {
            struct AVLNode* temp = root->left ? root->left : root->right;
            if (temp == NULL) {
                temp = root;
                root = NULL;
            } else {
                *root = *temp;
            }
            free(temp);
        } else {
            struct AVLNode* minNode = findMinNode(root->right);
            root->data = minNode->data;
            root->right = deleteNode(root->right, minNode->data);
        }
    }

    if (root == NULL) {
        return root;
    }

    return balanceNode(root);
}
void inorderTraversal(struct AVLNode* root) {
    if (root != NULL) {
        inorderTraversal(root->left);
        printf("%d ", root->data);
        inorderTraversal(root->right);
    }
}
struct AVLNode* insert(struct AVLNode* root, int value) {
    if (root == NULL) {
        return createNode(value);
    }

    if (value < root->data) {
        root->left = insert(root->left, value);
    } else if (value > root->data) {
        root->right = insert(root->right, value);
    } else {
        return root;
    }

    return balanceNode(root);
}

int main() {
    struct AVLNode* root = NULL;

    root = insert(root, 10);
    root = insert(root, 20);
    root = insert(root, 30);
    root = insert(root, 40);
    root = insert(root, 50);
    root = insert(root, 25);

    printf("In-order traversal: ");
    inorderTraversal(root);
    printf("\n");

    root = deleteNode(root, 30);
    printf("In-order traversal after deletion: ");
    inorderTraversal(root);
    printf("\n");

    return 0;
}
