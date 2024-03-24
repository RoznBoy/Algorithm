import sys
input = sys.stdin.readline

finger = int(input())
num = int(input())

# 첫번째 풀이
# 마지막 예제가 안됨;; 이유를 모르겠음
# 에라 모르겠다 채점해보자 -> 시간초과 
'''
finger_list = []
cnt = 1
flag = True
while True:
    finger_list.append(cnt)
    
    if flag:
        cnt += 1
    else:
        cnt -= 1
    # 5나 1에서 상태 변화 필요    
    if cnt == 5:
        flag = False
    elif cnt == 1:
        flag = True
        
    if finger_list.count(finger) == num+1:
        break    
    
print(len(finger_list)-1)
'''

# 두번째 풀이 시간을 줄이는 방법을 모르겠어서 검색하여 도움받음
# 단순히 프로그래밍 기능을 활용하는 것이 아니라 문제 자체에서 규칙성을 찾음
'''
1. hurtFinger가 1일 경우
: 만약 maxRepeat가 0이면 0을 출력하면 되고, 1 이거나 그 이상이면 8의 배수처럼 증가하는 것을 볼 수 있다.
maxRepeat가 1일 경우 : 1,2,3,4,5,4,3,2로 8개
maxRepeat가 2일 경우 : 1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2 16개 ...
maxRepeat가 증가할때마다 8개씩 증가하는 것을 확인할 수 있다.

2. hurtFinger가 5일 경우
: 만약 maxRepeat가 0이면 4를 출력하면 되고, maxRepeat이 1 이상일 때부터 8의 배수로 늘어난다는 것을 확인할 수 있다. 
maxRepeat가 1일 경우 : 1,2,3,4,5,4,3,2,1,2,3,4로 12개
maxRepeat가 2일 경우 : ...,5,4,3,2,1,2,3,4로 20개
maxRepeat가 증가할 때마다 8개씩 증가하는 것을 확인할 수 있다.

3. hurtFinger가 2,3,4일 경우
: 만약 maxRepeat가 0이면 hurtFinger-1을 출력하면 되고 1이거나 그 이상이면 번호를 세는 방법이 1,2,3,4처럼 증가하고 있던건지 4,3,2 처럼 감소하고 있던건지를 파악한 다음 해당 hurtFinger를 이용해서 마지막 숫자를 세면 된다.


처음빼고는 숫자를 2,3,4,5 혹은 4,3,2,1로 4개만 세니깐 4*maxRepeat + 1을 해서 처음에 1을 세는 걸 카운트해준다.
maxRepeat % 2 ==0인 경우 : hurtFinger - 2(2인 이유는 2가 가장 작은 hurtFinger이기 때문)를 더해준다
maxRepeat % 2 ==1인 경우 : 4- hurtFinger를 더해준다.
'''
cnt = 0
if finger == 1:
    cnt += 8*num
elif finger == 5:
    cnt += 8*num+4
else:
    cnt += 4*num+1
    if num%2 == 0:
        cnt += finger-2
    else:
        cnt += 4-finger
        
print(cnt)