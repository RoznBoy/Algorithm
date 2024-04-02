import sys
input = sys.stdin.readline
'''
N = int(input())
a, b = map(int, input().split())
M = int(input())

family = list([] for _ in range(N+1))
for _ in range(M):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

visited = [0]*(N+1)
result = []
def relationship(start, end, relatioship_cnt):
    visited[start] += 1
    relatioship_cnt += 1
    
    if start == end:
        result.append(relatioship_cnt)
    
    for i in family[start]:
        if not visited[i]:
            relationship(i, end, relatioship_cnt)
            
relationship(a,b,0)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)
'''

### 정답을 찾아보고 색다른 접근법 확인
### 일반적인 DFS/BFS는 방문 여부를 확인하는 리스트가 존재
### 아래와 같은 방법은 방법 여부의 정보를 포함하면서 알고리즘 수행 횟수 정보도 포함

sys.setrecursionlimit(300000)

def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node]+1 # 이 부분이 핵심 내용
            dfs(n)
            
n = int(input())
graph = [[] for _ in range(n+1)]
s, e = map(int, input().split())
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
check = [0]*(n+1)
dfs(s)
print(check[e] if check[e] > 0 else -1)
    