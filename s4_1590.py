import sys
input = sys.stdin.readline

N, T = map(int, input().split())

'''
버스마다 출발 시간을 쭈욱 정렬해
정렬한 시간에서 터미널 도착 시간이 위치하는 부분을 찾아
모든 버스에서 찾은 값들 중 최소 값을 찾아 (버스 시간 - 도착 시간)
'''

### 첫번째 풀이 틀림
def bus_search(array, target, st_index, en_index):
    
    while st_index < en_index:
        mid = (st_index + en_index)//2 
        if array[mid] >= target:
            en_index = mid - 1

        else:
            st_index = mid+1
            
    return array[st_index]


result = []
for _ in range(N):
    start, interval, num = map(int, input().split())
    bus_time = []
    for i in range(num):
        bus_time.append(start+interval*i)
    res = bus_search(bus_time, T, 0, len(bus_time)-1)
    result.append(res-T)
    
if min(result) < 0:
    print(-1)
else:
    print(min(result))
        
            