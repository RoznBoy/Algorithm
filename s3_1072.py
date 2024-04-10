import sys
input = sys.stdin.readline
import math

X, Y = map(int, input().split())
Z = math.floor(((Y/X)*100))
print(Z)

'''
이분 탐색은 정렬된 범위에서 중앙값을 확인하며 범위를 반씩 줄여서 탐색
이 문제는 분명히 하나씩 값을 더해서 확인하면 시간초과가 뜰 것이다.

 *** 이분 탐색을 하기 위한 범위를 찾는 것이 중요 ***
 일단 문제에서 주어진 X의 최대 값이 10억이므로 이것을 범위로 설정
'''
start = 0
end = 1000000000
res = X

if Z >= 99: # 100%는 완전한 값이므로 될 수가 없음, 99부터 변하지 않음
    print(-1)
else:
    while start <= end:
        mid = (end-start)//2
        if math.floor((((Y+mid)/(X+mid))*100)) > Z:
            end = mid - 1
            res = mid
        else:
            start = mid + 1
    print(mid)