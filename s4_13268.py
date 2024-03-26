import sys
import math
input = sys.stdin.readline

# 첫 번째 풀이 -> 런타임 에러 발생 
'''
N = int(input())
interval = [1,1,1,2,2,1,1,2,3,3,2,1,1,2,3,4,4,3,2,1]
total = 5*len(interval)
for i in range(math.ceil(N/total)):
    complete = N//5
print(interval[complete])
'''

# 두번째 풀이 -> for문을 없앴으나 이 또한 런타임 에러
N = int(input())
interval = [1,1,1,2,2,1,1,2,3,3,2,1,1,2,3,4,4,3,2,1]*(math.ceil(N/100))
complete = N//5
print(interval[complete])