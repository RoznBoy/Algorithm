import sys
input = sys.stdin.readline

N, M = map(int, input().split())

faith = list([] for _ in range(N+1)) # 해킹하는 것

for _ in range(M):
    A, B = map(int, input().split())
    faith[B].append(A) # B를 해킹하면 A를 해킹할 수 있음

#### 첫번째 풀이 : 시간 초과
### 마지막 for 문에서 모든 노드를 전부 도는 것이 시간 초과의 원인이라 판단됨
### 찾아보니 모두 비슷하게 문제가 발생
### pypy로 제출해보라고 해서 했더니 성공,,,으잉??

def hacking(num):
    cnt = 1
    visited = [0]*(N+1)
    visited[num] = 1
    stack = []
    stack.append(num)
    while stack:
        com = stack.pop()
        for next_com in faith[com]:             
            if visited[next_com] != 1:
                visited[next_com] = 1
                stack.append(next_com)
                cnt += 1
    return cnt
    
cnt_list = [0]*(N+1)
for i in range(1,N+1):
    cnt = hacking(i)
    cnt_list[i] = cnt
    
max_value = max(cnt_list)
indices = [index for index, value in enumerate(cnt_list) if value == max_value]
sorted_indices = sorted(indices)
print(*sorted_indices) # 리스트를 출력할 때 앞에 별을 붙여주면 괄호 제거