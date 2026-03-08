# Advanced BFS Shortest Path (Artificial Intelligence)

This repository contains a Python implementation of the **Breadth First Search (BFS)** algorithm to find the **shortest path in an unweighted graph**.

## About the Algorithm

Breadth First Search (BFS) is a graph traversal algorithm that explores nodes level by level.
It uses a **queue data structure** to visit nodes in the correct order.

BFS guarantees the **shortest path between two nodes in an unweighted graph**.

## Features of This Program

* Graph input taken from the **user**
* Uses **queue (BFS traversal)**
* Tracks **visited nodes**
* Reconstructs the **shortest path**
* Calculates the **distance between nodes**

## Requirements

* Python 3.x

## How to Run

Run the program using Python:

```
python advanced_bfs_shortest_path.py
```

## Example Input

```
Enter number of nodes: 5
Enter node: A
Enter neighbors separated by space: B C
Enter node: B
Enter neighbors separated by space: D
Enter node: C
Enter neighbors separated by space: E
Enter node: D
Enter neighbors separated by space:
Enter node: E
Enter neighbors separated by space: D
Enter start node: A
Enter goal node: D
```

## Example Output

```
Shortest Path: A -> B -> D
Distance: 2
```

## Author

Jagadeshwar Surneni
