# Adjacency List
In the first assignment, we created a graph using an adjacency matrix:

Attempt | 0 | 1 | 2 | 3 | 4 | 
:---: | :---: | :---: | :---: |:---: |:---: 
0 | False | True | False | False | True 
1 | True | False | True | True | True 
2 | False | True | False | True | False 
3 | False | True | True | False | True 
4 | True | True | False | True | False 

Through the rest of this course, we'll primarily be using an [adjacency list](https://en.wikipedia.org/wiki/Adjacency_list) instead. An adjacency list stores a list of vertices for each vertex that indicates where the connections are:

| Node | Connects With       |
|:-----:|---------------------|
| 0    | 1, 4                |
| 1    | 0, 2, 3, 4          |
| 2    | 1, 3                |
| 3    | 1, 2, 4             |
| 4    | 0, 1, 3             |

## Assignment
Let's rebuild our Graph class using an adjacency list.
1. Complete the constructor:
    - It should create an empty dictionary called graph as a data member.
2. Complete the add_edge method. It takes two vertices as inputs, and adds an edge to the adjacency list (the dictionary):
    - Be sure to map both vertices to each other, it's a bidirectional edge.
    - Handle the case where a set for a vertex doesn't exist yet.
    - The resulting graph maps vertices to a set of all other vertices they share an edge with. For example:
    ```
    result = {
        0: {1, 4},
        1: {0, 2, 3, 4},
        2: {1, 3},
        3: {1, 2, 4},
        4: {0, 1, 3}
    }
    ```