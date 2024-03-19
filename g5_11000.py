import sys
input = sys.stdin.readline

N = int(input())

### 첫번째 풀이 -> 시간 초과
study = []
for _ in range(N):
    study.append(list(map(int,input().split())))
study = sorted(study, key=lambda x: x[0]) # 이중 리스트 첫번째 요소 기준으로 오름차순 정렬
# print(study)

room = []
for i in range(len(study)):
    if not room:
        room.append(study[i][1])
    else:
        if min(room) <= study[i][0]:
            del room[room.index(min(room))]
            room.append(study[i][1])
        else:
            room.append(study[i][1])
print(len(room))

## 두번째 풀이
### 시간 초과를 해결하는 방법을 생각하지 못하여 정답 확인
### 확인해 본 정답 전부 패키지 사용;;
import heapq

lecture = sorted([list(map(int, input().split())) for _ in range(N)])
room = []
heapq.heappush(room,lecture[0][1]) # 첫 강의 끝나는 시간

for i in range(1,N):
    if lecture[i][0] < room[0]: # 강의의 시작 시간이 현재 강의 끝나는 시간 보다 짧으면
        heapq.heappush(room, lecture[i][1]) # 새로운 강의실을 넣자
    else: #아니면
        heapq.heappop(room) # 기존 강의를 빼내고
        heapq.heappush(room, lecture[i][1]) #해당 강의를 넣자
        
print(len(room))