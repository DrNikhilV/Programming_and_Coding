#include <stdio.h>
#include <stdbool.h>

#define SIZE 5

int items[SIZE];
int front = -1, rear = -1;

bool isFull() 
{
  if ((front == rear + 1) || (front == 0 && rear == SIZE - 1))
    return true;
  return false;
}

bool isEmpty() 
{
  if (front == -1)
    return true;
  return false;
}

void enQueue(int element) 
{
  if (isFull())
    printf("\n Queue is full\n");
  else 
  {
    if (front == -1)
      front = 0;
    rear = (rear + 1) % SIZE;
    items[rear] = element;
    printf("\n Inserted -> %d", element);
  }
}

int deQueue() 
{
  int element;
  if (isEmpty()) 
  {
    printf("\n Queue is empty\n");
    return (-1);
  } 
  else 
  {
    element = items[front];
    if (front == rear) 
    {
      front = -1;
      rear = -1;
    } 
    else 
    {
      front = (front + 1) % SIZE;
    }

    printf("\n Deleted element -> %d \n", element);
    return (element);
  }
}

void display() 
{
  int i;
  if (isEmpty())
    printf(" \n Empty Queue\n");
  else 
  {
    for (i = front; i != rear; i = (i + 1) % SIZE) {
    printf("%d ->", items[i]);
    }
    printf("%d ", items[i]);
  }
}

int main() 
{
  int choice, element;

  while (1) 
  {
    printf("\n1.Insert");
    printf("\n2.Delete");
    printf("\n3.Display");
    printf("\n4.Exit");
    printf("\nEnter your choice: ");
    scanf("%d", &choice);

    switch (choice) 
    {
      case 1:
        printf("\nEnter the element to be inserted: ");
        scanf("%d", &element);
        enQueue(element);
        break;

      case 2:
        deQueue();
        break;

      case 3:
        display();
        break;

      case 4:
        printf("\n Exit\n");
        return 0;

      default:
        printf("\n Invalid input\n");
    }
  }
}
