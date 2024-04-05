import sys
input = sys.stdin.readline

'''
아예 어떻게 접근해야할지 감이 안잡히네;;
일단 가장 큰 크레인이 가장 큰 박스를 먼저 이동하는 방식으로 가보자
한번 쓸 때, 크레인을 전부 다써야 효율적
반복문이 많아서 시간 초과 뜰 것이라 예상 ->> pypy3로 해결
'''

N = int(input())

crane = list(map(int, input().split()))
crane.sort(reverse=True)

M = int(input())

box = list(map(int, input().split()))
box.sort(reverse=True)

if crane[0] < box[0]:
    print(-1)
else:
    time = 0
    while box:
        for i in crane:
            for j in box:
                if i >= j:
                    box.remove(j) # remove는 리스트의 요소를 제거
                    break
        time += 1
    print(time)
        