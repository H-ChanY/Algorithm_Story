import sys

input=sys.stdin.readline


def bfs(start,end):
    root = [start]
    global n
    global graph
    visit = [0 for _ in range(n+1)]
    way =  [0 for _ in range(n+1)]
    while root:
        k = root.pop(0)
        if k == end:
            break
        if visit[k] == 0:
            visit[k] = 1
            for i in graph[k]:
                root.append(i[0])
                way[i[0]] = way[k] + i[1]
    return way[end]
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


for _ in range(m):
    a,b = map(int, input().split())
    print(bfs(a,b))