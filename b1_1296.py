import sys
input = sys.stdin.readline

'''
뭐 특별히 어렵지 않아
그냥 숫자 세서 연산 해보자
최댓값이 여러개 일 때, 사전 순 맨 앞이 우승 -> 단순 sort
'''

name = input().rstrip()

N = int(input())

team_list = []
for _ in range(N):
    team = input().rstrip()
    love = name+team
    L = love.count('L')
    O = love.count('O')
    V = love.count('V')
    E = love.count('E')
    prob = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
    team_list.append((team,prob))
    
team_list.sort(key=lambda x:x[1])

max_value = team_list[-1][1]
win = []
for i in team_list:
    if i[1] == max_value:
        win.append(i)
win.sort()



print(win[0][0])