

from collections import defaultdict


class Graph():
    def __init__(self, vertices=None):
        self.V = vertices               # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    def addEdge(self, v, w):
        self.graph[v].append(w)      # Add w to v_s list
        self.graph[w].append(v)      # add v to w_s list

    def isCycle(self):
        # Mark all vertices not visited
        visited = {}
        for v in self.graph.keys():
            visited[v] = False

        # Call recursive func to detect cycle in different DFS
        for i in self.graph.keys():
            # Skip visited node
            if not visited[i]:
                if self.isCycleUtil(i, visited, -1):
                    return True

        return False

    def isCycleUtil(self, v, visited, parent):
        """
        The program does a simple DFS traversal of graph
        and graph is represented using adjacency list.
        The time complexity is O(V+E)
        :param v:
        :param visited:
        :param parent:
        :return:
        """
        # Mark current node as visited
        visited[v] = True

        # Recursive for all the vertices adjacent to current node
        for i in self.graph[v]:
            # if the node not visited, then recursive on this node
            if not visited[i]:
                if self.isCycleUtil(i, visited, v):
                    return True
            # If an adjacent vertex is visited and its parent is not current vertex(v)
            # then it is a cycle
            elif parent != i:
                return True

        # else, nothing find, then it has no cycle
        return False


graph = {
    'a': {'a2': {}, 'a3': {}},
    'b': {'b2': {}},
    'c': {}
}


def find_cycle(graph):
    g = Graph(6)
    g.addEdge('a', 'a2')
    g.addEdge('a', 'a3')
    g.addEdge('b', 'b2')

    g.addEdge('c', 'a')
    g.addEdge('c', 'b')
    g.addEdge('c', 'c')

    print(g.graph)

    return g.isCycle()


print(find_cycle(graph))