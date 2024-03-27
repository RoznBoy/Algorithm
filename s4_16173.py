import sys

N = int(sys.stdin.readline())
game_map = []
visited = []
for _ in range(N):
    game_map.append(list(map(int, input().split())))
    visited.append([0]*N)
    
print(game_map)

def jelly_dfs(game_map, visited, x,y):
    # 방문한 곳이 게임판을 벗어나거나 이미 벗어난 경우 
    if x<0 or x>N-1 or y<0 or y>N-1 or visited[x][y]==1:
        return
    
    # 방문한 곳이 -1, 즉 게임 끝
    if game_map[x][y] == -1:
        visited[x][y] == 1
        return
    
    # 위의 두 경우 모두 해당하지 않은 경우 방문 표시
    visited[x][y] == 1
    
    jelly_dfs(game_map, visited, x+game_map[x][y],y)
    jelly_dfs(game_map, visited, x,y+game_map[x][y])
    
jelly_dfs(game_map,visited,0,0)

if visited[N-1][N-1] == 1:
    print('HaruHaru')
else:
    print('Hing')