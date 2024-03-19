import sys
input = sys.stdin.readline

N = int(input())
loss = list(map(int,input().split()))

# 문제의 이해가 많이 어려워서 접근조차 못함
# 문제 이해 방법을 먼저 찾아보고 구현
# 첫번째 풀이 -> 출력 초과 -> 질문 게시판의 반례들 전부 실행해보았는데 제대로 결과 나옴
# 똑같은 코드 다시 채점했는데 성공! 이거 무슨 경우야?
loss.sort()
cost = []
if N%2 == 0:
    for i in range(N//2):
        cost.append(loss[i]+loss[N-i-1])
    res = max(cost)
else:
    cost.append(loss[-1])
    loss.pop()
    for i in range(len(loss)//2):
        cost.append(loss[i]+loss[len(loss)-i-1])
    res = max(cost)

print(res)
