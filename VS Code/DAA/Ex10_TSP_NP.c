#include <stdio.h>
#include <limits.h>

#define V 4 

int nearestNeighbor(int graph[V][V], int visited[], int vertex) {
    int minDist = INT_MAX;
    int nearestVertex;

    for (int i = 0; i < V; i++) {
        if (graph[vertex][i] < minDist && !visited[i]) {
            minDist = graph[vertex][i];
            nearestVertex = i;
        }
    }

    return nearestVertex;
}

void tspNearestNeighbor(int graph[V][V]) {
    int visited[V];
    int tour[V + 1];
    int totalDistance = 0;

    for (int i = 0; i < V; i++)
        visited[i] = 0;

    int currentVertex = 0;
    visited[currentVertex] = 1;

    int i = 0;
    tour[i++] = currentVertex;
    for (; i < V; i++) {
        int nearest = nearestNeighbor(graph, visited, currentVertex);
        tour[i] = nearest;
        totalDistance += graph[currentVertex][nearest];
        visited[nearest] = 1;
        currentVertex = nearest;
    }

    tour[i] = 0;
    totalDistance += graph[currentVertex][0];

    printf("Approximate TSP Tour using Nearest Neighbor Algorithm: ");
    for (int j = 0; j <= V; j++)
        printf("%d ", tour[j]);
    printf("\nTotal Distance: %d\n", totalDistance);
}

int main() {
    int graph[V][V] = {{0, 10, 15, 20},
                       {10, 0, 35, 25},
                       {15, 35, 0, 30},
                       {20, 25, 30, 0}};

    tspNearestNeighbor(graph);

    return 0;
}
