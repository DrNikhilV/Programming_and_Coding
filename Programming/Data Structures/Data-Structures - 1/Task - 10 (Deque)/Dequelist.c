#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
};

struct Deque {
    struct Node* front;
    struct Node* rear;
};

struct Node* createNode(int element) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = element;
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}

void addFront(struct Deque* deque, int element) {
    struct Node* newNode = createNode(element);

    if (deque->front == NULL) {
        deque->front = newNode;
        deque->rear = newNode;
    } else {
        newNode->next = deque->front;
        deque->front->prev = newNode;
        deque->front = newNode;
    }

    printf("\nInserted at the front: %d", element);
}

void addRear(struct Deque* deque, int element) {
    struct Node* newNode = createNode(element);

    if (deque->rear == NULL) {
        deque->front = newNode;
        deque->rear = newNode;
    } else {
        newNode->prev = deque->rear;
        deque->rear->next = newNode;
        deque->rear = newNode;
    }

    printf("\nInserted at the rear: %d", element);
}

int delFront(struct Deque* deque) {
    if (deque->front == NULL) {
        printf("\nDeque is empty.\n");
        return -1;
    }

    struct Node* temp = deque->front;
    int element = temp->data;

    if (deque->front == deque->rear) {
        deque->front = NULL;
        deque->rear = NULL;
    } else {
        deque->front = deque->front->next;
        deque->front->prev = NULL;
    }

    free(temp);
    printf("\nRemoved from the front: %d", element);
    return element;
}

int delRear(struct Deque* deque) {
    if (deque->rear == NULL) {
        printf("\nDeque is empty.\n");
        return -1;
    }

    struct Node* temp = deque->rear;
    int element = temp->data;

    if (deque->front == deque->rear) {
        deque->front = NULL;
        deque->rear = NULL;
    } else {
        deque->rear = deque->rear->prev;
        deque->rear->next = NULL;
    }

    free(temp);
    printf("\nRemoved from the rear: %d", element);
    return element;
}

void display(struct Deque* deque) {
    if (deque->front == NULL) {
        printf("\nDeque is empty.\n");
        return;
    }

    struct Node* current = deque->front;
    printf("\nDeque elements: ");
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

int count(struct Deque* deque) {
    int count = 0;
    struct Node* current = deque->front;
    while (current != NULL) {
        count++;
        current = current->next;
    }
    return count;
}

int main() {
    struct Deque deque;
    deque.front = NULL;
    deque.rear = NULL;

    addRear(&deque, 5);
    addFront(&deque, 12);
    addRear(&deque, 11);
    addFront(&deque, 5);
    addRear(&deque, 6);
    addFront(&deque, 8);

    printf("\nElements in the deque: ");
    display(&deque);

    int removedItem = delFront(&deque);
    printf("\nRemoved item: %d", removedItem);

    printf("\nElements in the deque after deletion: ");
    display(&deque);

    addRear(&deque, 16);
    addRear(&deque, 7);

    printf("\nElements in the deque after addition: ");
    display(&deque);

    removedItem = delRear(&deque);
    printf("\nRemoved item: %d", removedItem);

    printf("\nElements in the deque after deletion: ");
    display(&deque);

    int totalCount = count(&deque);
    printf("\nTotal number of elements in the deque: %d\n", totalCount);

    return 0;
}
