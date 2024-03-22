import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 마니또와 받는 학생을 각각 리스트 인덱스로 번호를 매김
# 받는 학생도 인덱싱 한 이유는 주어진 정보에서 이미 주인공의 마니또가 알려지면 'NOJAM'이니까
'''
student = [0]*N
manitto = [0]*N
for _ in range(M):
    a, b = map(int, input().split())
    student[a-1] += 1
    manitto[b-1] += 1

s = int(input())
student[s-1] += 1
# manitto[s-1] += 1
print(student, manitto)
if student[s-1] == 2: # 두번째 설명에 대한 코드
    print('NOJAM')
else:
    manitto_possible = manitto.count(0)-1
    if manitto_possible == 1:
        print('NOJAM')
    
    else:
        print(manitto_possible)
'''          
## 첫번째 풀이 틀림 -> 아니 왜 틀린거야 다 맞는데
## 반례를 확인해보니 안되는 경우가 있음
## 딱 이렇다 말은 못하겠으나 왜 틀린지는 알거 같음 -> 어떻게 수정해야할지 감이 안잡힘 -> 새로운 방법 시도해보자
manitto = {}
for _ in range(M):
    a, b = map(int, input().split())
    manitto[a] = b

s = int(input())

print(manitto)

