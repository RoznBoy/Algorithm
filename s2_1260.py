import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

concat = list([] for _ in range(N+1))

for _ in range(M):
    a, b = map(int, input().split())
    concat[a].append(b)
    concat[b].append(a)

## 첫번째 풀이 : 각 알고리즘을 돌면서 값을 리스트에 저장하여 처리 -> 뭔가 제대로 안되는 문제가 있는듯
## 저장하고 출력하는 2번 일하는 방법 말고 일단 방문하면 출력으로 면경

# dfs_list = []    
dfs_visited = [0]*(N+1)
def dfs(start):
    # dfs_list.append(start)
    dfs_visited[start] = 1
    print(start, end=" ")
    for next in concat[start]:
        if dfs_visited[next] != 1:
            dfs(next)

from collections import deque
# bfs_list = []
bfs_visited = [0]*(N+1)
def bfs(start):
    queue = deque([start])
    bfs_visited[start] += 1
        
    while queue:
        node = queue.popleft()
        # bfs_list.append(node)
        print(node, end=" ")
        for next in concat[node]:
            if bfs_visited[next] != 1:
                bfs_visited[next] += 1
                queue.append(next)



# dfs(V)
# # print(*dfs_list)          
# print()      
bfs(V)
# print(*bfs_list)

            
    