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
                temp->link = temp;
            } else {
                current = head;
                while (current->link != head) {
                    current = current->link;
                }
                temp->link = head;
                current->link = temp;
                head = temp;
            }
        } else {
            current = head;
            for (i = 1; i < pos - 1; i++) {
                current = current->link;
            }
            temp->link = current->link;
            current->link = temp;
        }
        num++;
    }

    printf("List after insertion: ");
    current = head;
    do {
        printf("%d ", current->data);
        current = current->link;
    } while (current != head);
    printf("\n");

    return 0;
}
