# 14940 쉬운 최단거리
import sys
from collections import deque
input = sys.stdin.readline

# Input
N, M = map(int, input().split())
fields = [list(map(int, input().split())) for _ in range(N)]

# Settings
dir = [(1,0), (-1,0), (0,-1), (0,1)]
def find_target():
    for i in range(N):
        for j in range(M):
            if fields[i][j] == 2:
                return (i, j)

# 목표 찾기
start_i, start_j = find_target()
# 최댓값
INF = 1000*1000
# 방문 위치 설정
visited = [[INF] * M for _ in range(N)]
visited[start_i][start_j] = 0

# BFS
que = deque([(start_i, start_j)])
while que:
    i, j = que.popleft()
    for di, dj in dir:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<M and fields[ni][nj] != 0 and visited[ni][nj] > visited[i][j] + 1:
            visited[ni][nj] = visited[i][j] + 1
            que.append((ni, nj))
# Output
for i in range(N):
    for j in range(M):
        if fields[i][j] == 0:   # 만약 갈 수 없는곳이면 0으로 표시
            print(0, end=" ")
        elif visited[i][j] == INF:  # 갈 수 있는 곳이지만 0으로 둘러쌓인 곳은 -1
            print(-1, end=" ") 
        else:
            print(visited[i][j], end=" ")   # 나머지는 경로 출력
    print()
