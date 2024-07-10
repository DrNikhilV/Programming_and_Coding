#include<stdio.h>
#include<stdlib.h>

struct Node {
    int data;
    struct Node* link;
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
            head->link = head;
            current = head;
        } else {
            temp = (struct Node*) malloc(sizeof(struct Node));
            temp->data = ele;
            temp->link = head;
            current->link = temp;
            current = temp;
        }
    }

    printf("List elements: ");
    current = head;
    do {
        printf("%d ", current->data);
        current = current->link;
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
            while (current->link != head) {
                current = current->link;
            }
            temp = head;
            head = head->link;
            current->link = head;
            free(temp);
        }
    } else {
        current = head;
        for (i = 1; i < pos - 1; i++) {
            current = current->link;
        }
        temp = current->link;
        current->link = temp->link;
        free(temp);
    }

    printf("List after deletion: ");
    if (head == NULL) {
        printf("List is empty.\n");
    } else {
        current = head;
        do {
            printf("%d ", current->data);
            current = current->link;
        } while (current != head);
        printf("\n");
    }

    return 0;
}
