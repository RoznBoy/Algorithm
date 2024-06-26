import sys
input = sys.stdin.readline

'''
아니 이게 뭔 소리야 문제가 이해가 안돼;;
약속시간을 도대체 왜 늦게 가는거야 극혐이네
마법사 N명이 있어. 이 시간 개념 없는 애들은 머글 한명과 미팅을 해
기다리는 시간을 최소화 하기 위해 약속 시간을 T씩 미룬다
기다리는 시간 = 먼저 도착한 사람이 늦게 도착한 사람이 도착할 때까지 기다리는 시간
약속 시간은 A 그러나 도착한 시간은 B, 약속을 미루는 시간은 T |A+T-B|의 합이 기다리는 시간의 합과 같다
|A1+T-B1|+|A2+T-B2|+|A3+T-B3| 이것이 최소가 되는 T 값 구하기 ---> 어라? A와 B의 값이 주어지니 그냥 방정식의 최소값 구하는 문제네? 어라?
Ai-Bi=Xi 라 하면 |T+X1|+|T+X2|와 같은 방정식 

*** 그래프를 그려봐서 규칙성 발견 ***
항이 짝수개 일때는 반드시 T 가 전부 소거되는 부분 발생 : 상수 함수 형태
감소 (소거 부분) 증가 ---> 소거 부분이 최소값을 같게 됨
소거 부분의 범위를 구하면 최솟값 개수 알 수 있음

항이 홀수개 일때는 항상 1차 함수 형태 ---> 최소값은 무조건 1개
'''

N = int(input())
time_list = []
for _ in range(N):
    a, b = map(int, input().split())
    time_list.append(a-b)
    
time_list.sort()
    
if N%2 == 1:
    print(1)
else:
    print(abs(time_list[N//2]-time_list[(N//2)-1])+1)