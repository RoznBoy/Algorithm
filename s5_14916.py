import sys
input = sys.stdin.readline

N = int(input())

### 첫번째 문제 풀이 ###
### 예제 문제도 맞고 반례들도 확인했는데 왜틀린거지... ###
'''
num5 = N//5
num_list = []
for i in range(num5):
    num2 = N-5*(i+1)
    if num2 % 2 == 0:
        cnt = (i+1+(num2//2))  
        num_list.append(cnt)
        
if not num_list:
    print(-1)
else:
    print(min(num_list))
'''
    
### 두번째 풀이 ###
### 더 작은 값을 채워주는 느낌으로 접근 ###
cnt = 0
while N > 0:
    # print(cnt)
    if N%5 == 0:
        cnt += N//5
        N -= 5*(N//5)
        # print('num5', N)
    else:
        cnt += 1
        N -= 2
        # print('num2', N)
        
if N < 0:
    print(-1)
else:
    print(cnt)