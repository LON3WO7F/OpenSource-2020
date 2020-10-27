"""
This is an implementation of depth first search in python on a graph structure implemented as a python dictionary.
The example graph shown is "illustrated" below:

   E
 / |
A--B--D
|     |
C-----F

"""


def dfs(visited, graph, node):
    """
    Simple DFS implementation that prints out the nodes as they are searched, and returns them in a list

    Args:
      graph: (key,value) python dictionary of individual nodes as keys and a list of their adjacent nodes as the values
      node: string representation of the node or key in the graph/dictionary

    Returns:
      nothing only prints for now
    """
    try:
        if node not in visited and graph[node] is not None and graph[node] is not []:
            print(node, end="->")
            visited.append(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(visited, graph, n)
    except Exception as e:
        raise Exception(f"Error finding: {e}")


if __name__ == "__main__":
    # DEMO
    graph = {
        "A": ["B", "C", "E"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["F", "B"],
        "E": ["A", "B"],
        "F": ["C", "D"],
    }

    # show the DFS path from node 'E'
    res = dfs([], graph, "E")

    print("\n\nNow showing result of failed test:")
    # starting at a node that is not in the graph
    try:
        res = dfs([], graph, "Z")
    except Exception as e:
        print(f"{e}")
