#include <stdio.h>
#include <stdlib.h>

#define MAX 5  // Define the maximum size of the circular queue

struct CircularQueue {
    int arr[MAX];
    int front;
    int rear;
};

void initQueue(struct CircularQueue* queue) {
    queue->front = -1;
    queue->rear = -1;
}

int isFull(struct CircularQueue* queue) {
    return (queue->rear + 1) % MAX == queue->front;
}

int isEmpty(struct CircularQueue* queue) {
    return queue->front == -1;
}

void enqueue(struct CircularQueue* queue, int data) {
    if (isFull(queue)) {
        printf("Queue overflow\n");
        return;
    }
    if (isEmpty(queue)) {
        queue->front = 0;
    }
    queue->rear = (queue->rear + 1) % MAX;
    queue->arr[queue->rear] = data;
}

int dequeue(struct CircularQueue* queue) {
    if (isEmpty(queue)) {
        printf("Queue underflow\n");
        return -1;
    }
    int data = queue->arr[queue->front];
    if (queue->front == queue->rear) {
        queue->front = -1;  // Queue is now empty
        queue->rear = -1;
    } else {
        queue->front = (queue->front + 1) % MAX;
    }
    return data;
}

void display(struct CircularQueue* queue) {
    if (isEmpty(queue)) {
        printf("Queue is empty\n");
        return;
    }
    int i = queue->front;
    while (i != queue->rear) {
        printf("%d ", queue->arr[i]);
        i = (i + 1) % MAX;
    }
    printf("%d\n", queue->arr[i]);
}

int main() {
    struct CircularQueue queue;
    initQueue(&queue);

    enqueue(&queue, 10);
    enqueue(&queue, 20);
    enqueue(&queue, 30);
    enqueue(&queue, 40);
    enqueue(&queue, 50); // Queue is now full

    printf("Queue elements: ");
    display(&queue);

    printf("Dequeued element: %d\n", dequeue(&queue));
    printf("Dequeued element: %d\n", dequeue(&queue));

    printf("Queue elements after dequeue: ");
    display(&queue);

    enqueue(&queue, 60);
    enqueue(&queue, 70); // Should not be added because the queue is full

    printf("Queue elements after enqueue: ");
    display(&queue);

    return 0;
}
