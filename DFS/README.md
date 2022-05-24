# DFS BFS 정리

## DFS

### DFS의 정의 

DFS는 한국어로는 깊이 우선 탐색이라고 한다. 
루트 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방식을 말한다. 

예시: 미로찾기 시 최대한 한 방향으로 갈 수 있을 때까지 간 뒤 갈 곳이 없게 되면 가장 가까운 갈림길로 돌아온다.
그리고 갈림길로부터 다시 다른 방향으로 탐색을 하는 것이 깊이 우선 탐색 방식이다. 



### 특징 
1. 모든 노드를 방문하고자 하는 경우에 해당 방법을 선택
2. 깊이 우선 탐색이 너비 우선 탐색보다 알고리즘이 간단함. 
3. 검색 속도 자체는 너비 우선 탐색에 비해 느림. 
4. 스택 또는 재귀함수로 구현. 



## BFS

### BFS의 정의

BFS는 한국어로는 넓이 우선 탐색이라고 한다. 
루트 노드(임의의 노드도 가능)에서 시작하여 인접한 노드를 먼저 탐색하는 방법
시작점으로 부터 가까운 노드를 먼저 방문하고 먼 노드를 나중에 방문하는 순회 방법

예시: 두 노드 사이의 최단 경로 찾을 때 사용

### 특징
1.큐를 이용해서 구현. 



### DFS와 BFS의 시간 복잡도
두 알고리즘의 시간 복잡도는 동일
결국 모든 노드를 검색해야하기 때문이다. 


### DFS BFS 활용한 문제 유형/응용
1. 그래프 정점을 모두 방문 
  * DFS를 사용하던 BFS를 사용하던 상관없음
2. 경로의 특징을 저장해야하는 경우
  * 예시: 1~9까지 가는 경로 구하는 경우 경로에 같은 곳을 들리면 안된다 등의 제한이 있으면 DFS를 사용해야함. 
3. 최단거리를 구해야 하는 문제일 경우
  * BFS를 사용해야 한다.
  * 물론 DFS로 찾을 수 있지만 그게 최단 거리인지는 확인할 수 없음.




```
graph ={
  1: [2,3,4],
  2: [5],
  3: [5],
  4: [],
  5: [6,7],
  6: [],
  7: [3],
}
# graph를 dictionary로 만듦. 


def recursive_dfs(v,visited=[]):
  visited.append(v) # 시작점 방문
  for a in graph[v]:
    if not a in visited: # 방문하지 않았다면 
      visited=recursive_dfs(a,visited)
  return visited


def iterative_dfs(start_v):
  visited=[]
  stack=[start_v]
  while stack:
    v=stack.pop()
    if v not in visited:
      visited.append(v)
      for w in graph[v]:
        stack.append(w)
  return visited



```


