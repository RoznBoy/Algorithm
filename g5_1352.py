import sys
input = sys.stdin.readline

N, P, Q = map(int, input().split())

### 첫번째 풀이 틀림 : 테스트 케이스를 통과하지 못함
### 시간 초과를 예상했는데 테스트 케이스 실패라니,,,
### 그런데 왜 틀린지 모르겠다
dp = [1]
for i in range(1,N):
    new = dp[i//P] + dp[i//Q]
    print(dp[i//P], dp[i//Q],new)
    dp.append(new)
    
print(dp[-1])