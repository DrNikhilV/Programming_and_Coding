#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void insert(struct Node** head, int data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    struct Node* temp = *head;
    new_node->data = data;
    new_node->next = *head;

    if (*head != NULL) {
        while (temp->next != *head) {
            temp = temp->next;
        }
        temp->next = new_node;
    } else {
        new_node->next = new_node; // For the first node
        *head = new_node;
    }
}

void printList(struct Node* head) {
    struct Node* temp = head;
    if (head != NULL) {
        do {
            printf("%d ", temp->data);
            temp = temp->next;
        } while (temp != head);
    }
    printf("\n");
}

int main() {
    struct Node* head = NULL;
    int num, ele, i;

    printf("Enter size of list: ");
    scanf("%d", &num);

    for (i = 0; i < num; i++) {
        printf("Enter the element: ");
        scanf("%d", &ele);
        insert(&head, ele);
    }

    printf("The elements of the circular linked list are:\n");
    printList(head);

    return 0;
}
