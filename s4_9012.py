import sys
input = sys.stdin.readline

N = int(input())

### 첫번째 문제 풀이 ###
'''
for _ in range(N):
    VPS = list(input().strip())
    
    cnt = 0 
    for i in range(len(VPS)):
        if VPS[i] == '(':
            cnt += 1
        else:
            cnt -= 1
    if cnt == 0:
        print('YES')
    else:
        print('NO')       
'''
### 틀림;; 이유가 무엇일까? -> 확인해보니 예제 문제도 완벽하게 수행 못함 ###

### 두번째 문제 풀이 ###
### 괄호 이외의 다른 문자가 들어왔을때에도 -1이 실행 되므로 괄호만 판단하게 변경 ###
### 문제 잘못 이해 -> 단순히 괄호가 짝이 되는 것이 아니라 '(' 이것이 먼저 들어와야 VPS 완성 ###

for _ in range(N):
    VPS = list(input().strip())
    
    stack = []
    flag = 0
    for i in range(len(VPS)):
        if VPS[i] == '(':
            stack.append(VPS[i])
        else:
            if not stack:
                print('NO')
                flag += 1
                break
            else:
                stack.pop()
    if flag == 0:
        if not stack:
            print('YES')
        else:
            print('NO')

### git test ###
