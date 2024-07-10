#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node {
    int data;
    struct Node* next;
};

struct Queue {
    struct Node* front;
    struct Node* rear;
};

bool isEmpty(struct Queue* queue) {
    return (queue->front == NULL);
}

void enQueue(struct Queue* queue, int element) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = element;
    newNode->next = NULL;

    if (isEmpty(queue)) {
        queue->front = newNode;
        queue->rear = newNode;
        newNode->next = newNode;  // Make it circular
    } else {
        newNode->next = queue->front;
        queue->rear->next = newNode;
        queue->rear = newNode;
    }

    printf("\nInserted -> %d", element);
}

int deQueue(struct Queue* queue) {
    int element;
    if (isEmpty(queue)) {
        printf("\nQueue is empty\n");
        return -1;
    } else if (queue->front == queue->rear) {
        element = queue->front->data;
        free(queue->front);
        queue->front = NULL;
        queue->rear = NULL;
    } else {
        struct Node* temp = queue->front;
        element = temp->data;
        queue->front = queue->front->next;
        queue->rear->next = queue->front;
        free(temp);
    }

    printf("\nDeleted element -> %d\n", element);
    return element;
}

void display(struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("\nEmpty Queue\n");
    } else {
        struct Node* current = queue->front;
        printf("\nQueue: ");
        do {
            printf("%d -> ", current->data);
            current = current->next;
        } while (current != queue->front);
        printf("\n");
    }
}

int main() {
    struct Queue queue;
    queue.front = NULL;
    queue.rear = NULL;

    int choice, element;

    while (1) {
        printf("\n1.Insert");
        printf("\n2.Delete");
        printf("\n3.Display");
        printf("\n4.Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("\nEnter the element to be inserted: ");
                scanf("%d", &element);
                enQueue(&queue, element);
                break;

            case 2:
                deQueue(&queue);
                break;

            case 3:
                display(&queue);
                break;

            case 4:
                printf("\nExit\n");
                return 0;

            default:
                printf("\nInvalid input\n");
        }
    }
}
