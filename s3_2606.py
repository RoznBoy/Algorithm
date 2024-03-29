import sys
input = sys.stdin.readline

# BFS는 인접한 노드를 먼저 방문하는 system

N = int(input())
pair = int(input())
concat = list([] for _ in range(N+1))
for _ in range(pair):
    a, b = map(int,input().split())
    concat[a].append(b)
    concat[b].append(a)
# print(concat)

def virus(start):
    visited = [0]*(N+1)
    visited[start] += 1
    stack = [] 
    stack.append(start)
    while stack:
        node = stack.pop()
        for next_node in concat[node]:
            if visited[next_node] != 1:
                visited[next_node] += 1
                stack.append(next_node)
    
    infect = visited.count(1)-1 
    return infect

print(virus(1))


