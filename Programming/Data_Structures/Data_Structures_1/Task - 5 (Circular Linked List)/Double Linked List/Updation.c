#include<stdio.h>
#include<stdlib.h>

struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
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
            head->prev = NULL;
            head->next = NULL;
            current = head;
        } else {
            temp = (struct Node*) malloc(sizeof(struct Node));
            temp->data = ele;
            temp->prev = current;
            temp->next = NULL;
            current->next = temp;
            current = temp;
        }
    }

    printf("List elements: ");
    current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");

    printf("Enter position to insert: ");
    scanf("%d", &pos);
    printf("Enter element to insert: ");
    scanf("%d", &ele);

    if (pos <= 0 || pos > num + 1) {
        printf("Invalid position.\n");
    } else {
        temp = (struct Node*) malloc(sizeof(struct Node));
        temp->data = ele;
        if (pos == 1) {
            if (head == NULL) {
                head = temp;
                temp->prev = NULL;
                temp->next = NULL;
            } else {
                temp->prev = NULL;
                temp->next = head;
                head->prev = temp;
                head = temp;
            }
        } else {
            current = head;
            for (i = 1; i < pos - 1; i++) {
                current = current->next;
            }
            temp->prev = current;
            temp->next = current->next;
            if (current->next != NULL) {
                current->next->prev = temp;
            }
            current->next = temp;
        }
        num++;
    }

    printf("List after insertion: ");
    current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");

    return 0;
}
