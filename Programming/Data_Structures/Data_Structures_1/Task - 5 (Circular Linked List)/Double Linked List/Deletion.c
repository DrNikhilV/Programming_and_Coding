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
    struct Node* current = NULL;

    int num, ele, i, pos;
    printf("Enter size of list: ");
    scanf("%d", &num);

    for (i = 0; i < num; i++) {
        printf("Enter the element: ");
        scanf("%d", &ele);

        if (head == NULL) {
            head = (struct Node*) malloc(sizeof(struct Node));
            head->data = ele;
            head->next = head;
            head->prev = head;
            current = head;
        } else {
            temp = (struct Node*) malloc(sizeof(struct Node));
            temp->data = ele;
            temp->next = head;
            temp->prev = current;
            current->next = temp;
            head->prev = temp;
            current = temp;
        }
    }

    printf("List elements: ");
    current = head;
    do {
        printf("%d ", current->data);
        current = current->next;
    } while (current != head);
    printf("\n");

    printf("Enter position to delete: ");
    scanf("%d", &pos);

    if (pos <= 0 || pos > num) {
        printf("Invalid position.\n");
    } else if (pos == 1) {

        if (num == 1) {
            free(head);
            head = NULL;
        } else {
            current = head;
            while (current->next != head) {
                current = current->next;
            }
            temp = head;
            head = head->next;
            current->next = head;
            head->prev = current;
            free(temp);
        }
    } else {
        current = head;
        for (i = 1; i < pos; i++) {
            current = current->next;
        }
        temp = current;
        current->prev->next = current->next;
        current->next->prev = current->prev;
        free(temp);
    }

    printf("List after deletion: ");
    if (head == NULL) {
        printf("List is empty.\n");
    } else {
        current = head;
        do {
            printf("%d ", current->data);
            current = current->next;
        } while (current != head);
        printf("\n");
    }

    return 0;
}
