import sys
input = sys.stdin.readline
N= int(input())

### 최소 힙 개념 관련 공부 사이트 : https://reakwon.tistory.com/42 ###
### 0이 들어오면 가장 작은 값을 출력 후 제거 ###
### 배열이 비어 있을 때 0이 들어오면 0 출력 ###

### 첫번째 풀이 ###
### 예제 문제는 맞게 풀었으나 시간초과 발생
'''
heap = []
for _ in range(N):
    num = int(input())
    
    if num > 0:
        heap.append(num)
        heap.sort(reverse=True)
    else:
        if not heap:
            print(0)
        else:
            print(heap[-1])
            heap.pop()
'''

### 두번째 풀이 ###
### 정답 검색 해 봄 -> 전부 heap 패키지 사용
import heapq
heap=[]
for i in range(N):
    x=int(sys.stdin.readline())

    if x!=0:
        heapq.heappush(heap,x)
    else:
        if len(heap)!=0:
            print(heapq.heappop(heap))
        else:
            print(0)
