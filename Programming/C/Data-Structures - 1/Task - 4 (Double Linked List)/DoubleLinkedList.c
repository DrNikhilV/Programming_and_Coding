#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
};

int main() {
    struct Node* head = NULL;
    struct Node* temp = NULL;
    struct Node* new_node = NULL;

    int num, ele, i;
    printf("Enter size of list: ");
    scanf("%d", &num);

    for (i = 0; i < num; i++) {
        printf("Enter the element: ");
        scanf("%d", &ele);

        new_node = (struct Node*)malloc(sizeof(struct Node));
        new_node->data = ele;
        new_node->next = NULL;
        new_node->prev = temp;

        if (temp != NULL) {
            temp->next = new_node;
        } else {
            head = new_node;
        }

        temp = new_node;
    }

    printf("The elements of the list are (forward):\n");
    temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");

    printf("The elements of the list are (backward):\n");
    if (head != NULL) {
        temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        
        while (temp != NULL) {
            printf("%d ", temp->data);
            temp = temp->prev;
        }
        printf("\n");
    }

    return 0;
}
