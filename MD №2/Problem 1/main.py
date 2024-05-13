def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]

    for pair in prerequisites:
        x, y = pair
        graph[x].append(y)

    for i in range(numCourses):
        if not dfs(graph, visited, i):
            return False

    return True


def dfs(graph, visited, i):
    if visited[i] == -1:
        return False

    if visited[i] == 1:
        return True

    visited[i] = -1
    print(graph)
    for j in graph[i]:
        if not dfs(graph, visited, j):
            return False

    visited[i] = 1

    return True


numCourses = int(input("Enter the num of courses: "))
prerequisites = eval(input("Enter the prerequisites: "))
print(canFinish(numCourses, prerequisites))
