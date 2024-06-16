#include <stdio.h>
#include <stdlib.h>

#define MAX 100

struct Deque {
    int arr[MAX];
    int front;
    int rear;
    int size;
};

void initDeque(struct Deque* deque) {
    deque->front = -1;
    deque->rear = 0;
    deque->size = 0;
}

int isFull(struct Deque* deque) {
    return deque->size == MAX;
}

int isEmpty(struct Deque* deque) {
    return deque->size == 0;
}

void insertFront(struct Deque* deque, int data) {
    if (isFull(deque)) {
        printf("Deque overflow\n");
        return;
    }
    if (deque->front == -1) {
        deque->front = 0;
        deque->rear = 0;
    } else if (deque->front == 0) {
        deque->front = MAX - 1;
    } else {
        deque->front--;
    }
    deque->arr[deque->front] = data;
    deque->size++;
}

void insertRear(struct Deque* deque, int data) {
    if (isFull(deque)) {
        printf("Deque overflow\n");
        return;
    }
    if (deque->front == -1) {
        deque->front = 0;
        deque->rear = 0;
    } else if (deque->rear == MAX - 1) {
        deque->rear = 0;
    } else {
        deque->rear++;
    }
    deque->arr[deque->rear] = data;
    deque->size++;
}

int deleteFront(struct Deque* deque) {
    if (isEmpty(deque)) {
        printf("Deque underflow\n");
        return -1;
    }
    int data = deque->arr[deque->front];
    if (deque->front == deque->rear) {
        deque->front = -1;
        deque->rear = -1;
    } else if (deque->front == MAX - 1) {
        deque->front = 0;
    } else {
        deque->front++;
    }
    deque->size--;
    return data;
}

int deleteRear(struct Deque* deque) {
    if (isEmpty(deque)) {
        printf("Deque underflow\n");
        return -1;
    }
    int data = deque->arr[deque->rear];
    if (deque->front == deque->rear) {
        deque->front = -1;
        deque->rear = -1;
    } else if (deque->rear == 0) {
        deque->rear = MAX - 1;
    } else {
        deque->rear--;
    }
    deque->size--;
    return data;
}

void display(struct Deque* deque) {
    if (isEmpty(deque)) {
        printf("Deque is empty\n");
        return;
    }
    int i = deque->front;
    while (i != deque->rear) {
        printf("%d ", deque->arr[i]);
        i = (i + 1) % MAX;
    }
    printf("%d\n", deque->arr[i]);
}

int main() {
    struct Deque deque;
    initDeque(&deque);

    insertRear(&deque, 10);
    insertRear(&deque, 20);
    insertFront(&deque, 5);
    insertFront(&deque, 2);

    printf("Deque elements: ");
    display(&deque);

    printf("Deleted from front: %d\n", deleteFront(&deque));
    printf("Deleted from rear: %d\n", deleteRear(&deque));

    printf("Deque elements after deletions: ");
    display(&deque);

    return 0;
}
