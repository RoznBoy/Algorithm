import sys
input = sys.stdin.readline

N, T = map(int, input().split())

'''
버스마다 출발 시간을 쭈욱 정렬해
정렬한 시간에서 터미널 도착 시간이 위치하는 부분을 찾아
모든 버스에서 찾은 값들 중 최소 값을 찾아 (버스 시간 - 도착 시간)
'''

### 첫번째 풀이 틀림 -> 테스트 사례 다 맞고 뭐가 틀린거지 모르겠다
### 반례 찾아서 수정 while문 기준에 같을 때, 추가 ->
### 런타임 에러
'''
def bus_search(array, target, st_index, en_index):
    
    while st_index <= en_index:
        mid = (st_index + en_index)//2 
        if array[mid] >= target:
            check = mid
            en_index = mid - 1

        else:
            st_index = mid + 1
            
    return array[check]


result = []
for _ in range(N):
    start, interval, num = map(int, input().split())
    bus_time = []
    for i in range(num):
        bus_time.append(start+interval*i)
    print(len(bus_time))
    res = bus_search(bus_time, T, 0, len(bus_time)-1)
    result.append(res-T)
'''    

result = []
for _ in range(N):
    start, interval, num = map(int, input().split())
    bus_time = []
    for i in range(num):
        bus_time.append(start+interval*i)
    # print(len(bus_time))
    
    while st_index <= en_index:
        mid = (st_index + en_index)//2 
        if bus_time[mid] >= T:
            check = mid
            en_index = mid - 1

        else:
            st_index = mid + 1
    
    result.append(bus_time[check]-T)
    
if min(result) < 0:
    print(-1)
else:
    print(min(result))
        
            