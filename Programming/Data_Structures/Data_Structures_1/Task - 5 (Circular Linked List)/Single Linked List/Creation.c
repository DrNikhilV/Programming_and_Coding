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

    int num, ele, i;
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

    return 0;
}
