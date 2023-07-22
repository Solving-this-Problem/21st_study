# 14940_쉬운 최단거리
import sys
from collections import deque
input = sys.stdin.readline

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

x, y = 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            x, y = i, j
            break

q = deque()
q.append([x, y, 0])
visited[x][y] = 0

while q:
    lx, ly, dis = q.popleft()

    for d in dxy:
        nx = lx + d[0]
        ny = ly + d[1]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1 and visited[nx][ny] == -1:
                q.append([nx, ny, dis+1])
                visited[nx][ny] = dis+1

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            visited[i][j] = 0

for v in visited:
    print(*v)