## BFS 1
graph = {
    'Amin'    : {'Wasim', 'Nick', 'Mike'},
    'Wasim'   : {'Imran', 'Amin'},
    'Imran'   : {'Wasim', 'Faras'},
    'Faras'   : {'Imran'},
    'Mike'    : {'Amin'},
    'Nick'     : {'Amin'}}

def BFS(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

BFS(graph, 'Amin')

## BFS 2
graph = {
    'Amin'    : {'Wasim', 'Nick', 'Mike'},
    'Wasim'   : {'Imran', 'Amin'},
    'Imran'   : {'Wasim', 'Faras'},
    'Faras'   : {'Imran'},
    'Mike'    : {'Amin'},
    'Nick'     : {'Amin'}}

def BFS(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

BFS(graph, 'Amin')

## DFS 1
graph = {
    'Amin'    : {'Wasim', 'Nick', 'Mike'},
    'Wasim' : {'Imran', 'Amin'},
    'Imran'   : {'Wasim', 'Faras'},
    'Faras'   : {'Imran'},
    'Mike'    : {'Amin'},
    'Nick'     : {'Amin'}}

def DFS(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    
    ## 순회 경로
    for next in graph[start] - visited:
        DFS(graph, next, visited)
    return visited

DFS(graph, 'Amin')  

## DFS 2
graph = {
    'Amin'    : {'Wasim', 'Nick', 'Mike'},
    'Wasim' : {'Imran', 'Amin'},
    'Imran'   : {'Wasim', 'Faras'},
    'Faras'   : {'Imran'},
    'Mike'    : {'Amin'},
    'Nick'     : {'Amin'}}

def DFS(graph, Start):
    visited = []
    stack = [Start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)

DFS(graph, "Amin")
