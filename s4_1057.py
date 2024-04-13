import sys
input = sys.stdin.readline

N, kim, im = map(int, input().split())

'''
8명의 참가자가 있을 때
라운드가 진행되면 각 번호가 반으로 줄어든다.
1 2 3 4 5 6 7 8 
1 1 2 2 3 3 4 4 
만나고자 하는 두 팀이 같은 번호가 되었을 때 만나게 됨
'''

round = 0
while kim != im:
    kim -= kim//2
    im -= im//2
    round += 1

print(round)
    