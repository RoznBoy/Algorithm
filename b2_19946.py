import sys
import math
input = sys.stdin.readline
'''
N = int(input())
# 첫번째 풀이
# 입력 값을 2로 나누다 보면 2의 배수가 아닌 곳 발생 -> 이 지점 찾기
# 반례가 없어서 여러 값을 임의로 넣어서 해보았는데 맞음
# 이유가 뭘까?
power = math.ceil(math.log2(N+1)) # 2^1 일 때 잘못 계산하면 똑같이 2의 거듭제곱 형태라서 잘 찾아주지 못함
# print(power)
while True:
    if N%2 == 0:
        N = N/2
        power -= 1
    else:
        break
    
print(power)
'''
# 정답 찾아본 풀이
# 왜 64로 고정하는지 이해가 안됨
n = int(input())
k = 64
while n % 2 == 0:
    n //= 2
    k -= 1
print(k)