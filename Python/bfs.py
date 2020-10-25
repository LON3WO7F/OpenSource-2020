"""
This is an implementation of breadth first search in python on a graph structure implemented as a python dictionary.
The example graph shown is "illustrated" below:

   E
 / |
A--B--D
|     |
C-----F

"""


def bfs(graph: dict, node: str):
    """
    Simple BFS implementation that prints out the nodes as they are searched, and returns them in a list

    Args:
      graph: (key,value) python dictionary of individual nodes as keys and a list of their adjacent nodes as the values
      node: string representation of the node or key in the graph/dictionary

    Returns:
      List of nodes in the order they were searched (BFS)
      or and Exception if the starting node was not found
    """

    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    results = []
    while queue:
        s = queue.pop(0)
        if s in graph.keys():
            print(s, end="->")
            results.append(s)
            for n in graph[s]:
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
        else:
            raise Exception("Node not found in graph")
    print("END")
    return results


# DEMO
graph = {"A": ["B", "C", "E"], "B": ["A", "D", "E"], "C": ["A", "F"], "D": ["F", "B"], "E": ["A", "B"], "F": ["C", "D"]}

# show the BFS path from node 'E'
res = bfs(graph, "E")

# starting at a node that is not in the graph
try:
    res = bfs(graph, "Z")
except Exception as e:
    print(f"{e}")
