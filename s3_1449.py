import sys
input = sys.stdin.readline

'''
문제 이해 
현승이가 가지고 있는 테이프의 길이 L=2일 때, 누수지점 1, 2, 100, 101
1 -> 0.5~1.5, 2-> 1.5~2.5 : 누수 지점 1과 2는 2짜리 테이프 하나로 막을 수 있음
100과 101 마찬가지
테이프 자르는 건 안되고, 겹치는건 가능
문제 이해는 했으나 접근 방법 생각 어렵네;;
좀 검색해보니 테이프를 업데이트 해주는 지점을 설정하는 방법 사용해보자
'''

N, L = map(int, input().split())

location = list(map(int, input().split()))
location.sort()
# print(location)

start = location[0]
cnt = 1

for i in location[1:]:
    if i in range(start, start+L):
        continue
    else:
        start = i
        cnt += 1
        
print(cnt)
