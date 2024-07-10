#include <stdio.h>
#include <stdlib.h>

struct Queue {
    int front, rear, size;
    unsigned capacity;
    int* array;
};

struct Queue* createQueue(unsigned capacity) {
    struct Queue* queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->capacity = capacity;
    queue->front = queue->size = 0;
    queue->rear = capacity - 1;
    queue->array = (int*)malloc(queue->capacity * sizeof(int));
    return queue;
}

int isFull(struct Queue* queue) {
    return (queue->size == queue->capacity);
}

int isEmpty(struct Queue* queue) {
    return (queue->size == 0);
}

void enqueue(struct Queue* queue, int item) {
    if (isFull(queue)) {
        printf("Queue is full\n");
        return;
    }
    queue->rear = (queue->rear + 1) % queue->capacity;
    queue->array[queue->rear] = item;
    queue->size++;
}

int dequeue(struct Queue* queue) {
    if (isEmpty(queue)) {
        printf("Queue is empty\n");
        return -1;
    }
    int item = queue->array[queue->front];
    queue->front = (queue->front + 1) % queue->capacity;
    queue->size--;
    return item;
}

int getTicketTime(int* tickets, int n, int k) {
    struct Queue* queue = createQueue(n);

    for (int i = 0; i < n; i++) {
        enqueue(queue, tickets[i]);
    }

    int time = 0;
    while (!isEmpty(queue)) {
        int currentPerson = dequeue(queue);
        if (currentPerson > 0) {
            enqueue(queue, currentPerson - 1);
        }
        if (k == 0) {
            time++;
            if (currentPerson == 0) {
                break;
            }
        } else {
            if (currentPerson > 0) {
                enqueue(queue, currentPerson - 1);
            }
            k--;
        }
        time++;
    }

    return time;
}

int main() {
    int n;
    printf("Enter the number of people in the queue: ");
    scanf("%d", &n);

    int* tickets = (int*)malloc(n * sizeof(int));

    printf("Enter the number of tickets each person wants to buy:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &tickets[i]);
    }

    int k;
    printf("Enter the position of the person you want to calculate the time for: ");
    scanf("%d", &k);

    int time = getTicketTime(tickets, n, k);

    printf("Time taken for person at position %d: %d seconds\n", k, time);

    free(tickets);

    return 0;
}
