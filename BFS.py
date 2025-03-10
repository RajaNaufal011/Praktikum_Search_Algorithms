# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-k3DJ5orcitK--ya4UK-ebzCF2uyzVJv
"""

# -*- coding: utf-8 -*-
"""BFS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mPgJnrWJLoikY6fhR9lpjsLvAGi1W8cj
"""

import collections

# BFS algorithm
def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + "", end=" ")
        # If not visited, mark it as visited, and enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    graph = {'R': ['N', 'F'], 'N': ['F'], 'F': ['A'], 'A': ['N', 'F']}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 'R')