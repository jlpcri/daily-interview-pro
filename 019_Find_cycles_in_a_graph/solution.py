def find_cycle(graph):
    visited = []
    for i in graph.keys():
        if i not in visited:
            if isCycle(i, visited, -1):
                return True

    return False


def isCycle(child, visited, parent):
    visited.append(child)

    if child not in graph.keys():
        return

    for i in graph[child].keys():
        if i not in visited:
            if isCycle(i, visited, child):
                return True
        elif parent != child:
            return True

    return False


graph = {
  'a': {'a2':{}, 'a3':{} },
  'b': {'b2':{}},
  'c': {}
}
print(find_cycle(graph))
# False
graph['c'] = graph
print(find_cycle(graph))
# True
