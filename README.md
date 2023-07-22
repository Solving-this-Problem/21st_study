# 21th_study
[21주차] 코딩테스트 준비 9주차
<br/>

[프로그래머스 python 문제 바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/77485)

[백준 문제집 바로가기](https://www.acmicpc.net/workbook/view/16147)

<br/><br/>

# [프로그래머스] 행렬 테두리 회전하기

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./행렬%20테두리%20회전하기/동우.py)
```py
```
## [민웅](./행렬%20테두리%20회전하기/민웅.py)
```py
def solution(rows, columns, queries):
    answer = []
    mat = []
    num = 1
    for i in range(rows):
        lst = []
        for j in range(columns):
            lst.append(num)
            num += 1
        mat.append(lst)
    # print(mat)

    for query in queries:
        sx, sy, ex, ey = query
        m_value = float('inf')
        temp = mat[sx-1][sy-1]
        change = (2*(ex-sx+1)+2*(ey-sy+1)-4)
        i, j = sx-1, sy-1
        while change:
            if i == sx-1 and j == sy-1:
                while j != ey-1:
                    mat[i][j+1], temp = temp, mat[i][j+1]
                    j += 1
                    change -= 1
                    if temp < m_value:
                        m_value = temp
            elif i == sx-1 and j == ey-1:
                while i != ex-1:
                    mat[i+1][j], temp = temp, mat[i+1][j]
                    i += 1
                    change -= 1
                    if temp < m_value:
                        m_value = temp
            elif i == ex-1 and j == ey-1:
                while j != sy-1:
                    mat[i][j-1], temp = temp, mat[i][j-1]
                    j -= 1
                    change -= 1
                    if temp < m_value:
                        m_value = temp
            else:
                while i != sx-1:
                    mat[i-1][j], temp = temp, mat[i-1][j]
                    i -= 1
                    change -= 1
                    if temp < m_value:
                        m_value = temp
        answer.append(m_value)
    return answer
```
## [서희](./행렬%20테두리%20회전하기/서희.py)
```py
```
## [성구](./행렬%20테두리%20회전하기/성구.py)
```py
# 행렬 테두리 회전하기     
def solution(rows, columns, queries):
    answer = []
    # 사용할 2차원 배열
    matrix = [[j + columns*i for j in range(1, columns+1)] for i in range(rows)]
    # 기존과 비교할 2차원 배열
    arr = [[0] * columns for _ in range(rows)]
    for quest in queries:
        i, j = quest[0]-1, quest[1]-1
        # 이전값 저장
        tmp = matrix[i+1][j]
        # 이전 2차원 배열 저장
        for arri in range(rows):
            for arrj in range(columns):
                arr[arri][arrj] = matrix[arri][arrj]
        # 회전~~~~회오리이이ㅣ
        while True:
            tmp, matrix[i][j]  = matrix[i][j], tmp
            if i == quest[0]-1:
                if j == quest[1]-1:
                    j += 1
                elif j == quest[3]-1:
                    i += 1
                else:
                    j += 1
            elif j == quest[3]-1:
                if i ==quest[2]-1:
                    j -=1
                else:
                    i +=1
            elif i == quest[2]-1:
                if j == quest[1]-1:
                    i -= 1
                else:
                    j -=1 
            elif j == quest[1]-1:
                if i == quest[0]-1:
                    break
                else:
                    i -= 1
            if i == quest[0]-1 and j == quest[1] -1:
                break
        # 최소 찾기
        minV = 10001
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] != arr[i][j] and minV > arr[i][j] :
                    minV = arr[i][j]
        # 최소 저장
        answer.append(minV)
    return answer
```
## [혜진](./행렬%20테두리%20회전하기/혜진.py)
```py
```

</div>
</details>

<br/><br/><br/>

# [백준] 크로스 컨트리

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./크로스%20컨트리/동우.py)
```py
```
## [민웅](./크로스%20컨트리/민웅.py)
```py
# 9017_크로스컨트리_CrossCountry
import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N = int(input())

    players = list(map(int, input().split()))
    teams = {}
    scores = {}
    m_value = 0
    fifth_p = float('inf')
    ans = 0

    for i in range(N):
        if players[i] in teams.keys():
            teams[players[i]].append(i)
            if len(teams[players[i]]) <= 4:
                scores[players[i]] += (i+1)
        else:
            teams[players[i]] = [i]
            scores[players[i]] = (i+1)

    for k in teams.keys():
        if len(teams[k]) == 6:
            if scores[k] > m_value:
                m_value = scores[k]
                fifth_p = teams[k][4]
                ans = k
            elif scores[k] == m_value:
                if teams[k][4] < fifth_p:
                    ans = k
                    fifth_p = teams[k][4]

    print(ans)
```
## [서희](./크로스%20컨트리/서희.py)
```py
```
## [성구](./크로스%20컨트리/성구.py)
```py
# 9017 크로스 컨트리
import sys
input = sys.stdin.readline

# testcase
for _ in range(int(input())):
    # Input
    N = int(input())
    rank = list(map(int,input().split()))
    # define
    num = {}    # 팀 멤버 수
    team = {}   # 6명 이상의 팀의 점수 리스트
    cnt = 1     # 1등 부터 시작하므로 1
    
    # num, team 세팅
    for i in range(N):
        if rank[i] not in num.keys():   
            num[rank[i]] = 1
        else:
            num[rank[i]] += 1
    for i in rank:
        if num[i] >= 6:
            if i not in team.keys():
                team[i] = [cnt]
            else:
                team[i].append(cnt)
            cnt +=1
    # 최소를 찾기위한 세팅
    minS = 4000
    idx = -1    # 최소의 key 값

    for key, val in team.items():
        score = sum(val[:4])
        if minS > score:        # 점수가 더 낮으면 우승팀을 바꿈
            minS = score
            idx = key
        elif minS == score:     # 점수가 같으면 5번째 선수 점수가 더 낮은 팀이 우승
            if team[idx][4] > val[4]:
                maxS = score
                idx = key

    # Output 우승 팀
    print(idx)
```
## [혜진](./크로스%20컨트리/혜진.py)
```py
```

</div>
</details>

<br/><br/><br/>


# [백준] 쉬운 최단거리

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./쉬운%20최단거리/동우.py)
```py
```
## [민웅](./쉬운%20최단거리/민웅.py)
```py
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
```
## [서희](./쉬운%20최단거리/서희.py)
```py
```
## [성구](./쉬운%20최단거리/성구.py)
```py
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
```
## [혜진](./쉬운%20최단거리/혜진.py)
```py
```

</div>
</details>

<br/><br/><br/>


# [백준] 고층 건물

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./고층건물/동우.py)
```py
```
## [민웅](./고층건물/민웅.py)
```py
# 1027_고층건물_skyscraper
import sys
input = sys.stdin.readline
# 접하면 안된다 -> 같은 직선상에 있는 같은 기울기 선분도 안된다

N = int(input())

nli = list(map(int, input().split()))

check = [0]*50

for i in range(N):
    right, left = float('-inf'), float('inf')
    for j in range(i+1, N):
        temp = (nli[j] - nli[i]) / (j - i)
        if nli[j] >= nli[i]:
            if temp > right:
                check[i] += 1
                check[j] += 1
                right = temp
        # if j == i+1:
        #     if nli[j] == nli[i]:
        #         check[i] += 1
        #         check[j] += 1

    for k in range(i-1, -1, -1):
        temp = (nli[k] - nli[i]) / (k - i)
        if nli[k] > nli[i]:
            if temp < left:
                check[i] += 1
                check[k] += 1
                left = temp

print(max(check))
```
## [서희](./고층건물/서희.py)
```py
```
## [성구](./고층건물/성구.py)
```py
# 1027 고층건물

'''
0 < N <=50
0 < buildings[] <= 1000000000
'''
import sys
input = sys.stdin.readline

# Input
N = int(input())
buildings = list(map(int, input().split()))

# Setting
# 보이는 건물들 카운트 리스트
cnt = [0]*N

# 내가 보이는 건물과의 각도가 최대인 것만 체크
# 내가 볼 수 있는 건물은 반대에서도 볼 수 있음
# 따라서 최대일 때 최댓값 갱신 및 두 건물의 cnt ++
for i in range(N):
    maxAngle = -1000000001
    for j in range(i+1, N):
        angle = (buildings[i]-buildings[j]) / (i-j)
        if angle > maxAngle:
            maxAngle = angle
            cnt[i] += 1
            cnt[j] += 1

# Output
# 최댓값만 출력
print(max(cnt))            
```
## [혜진](./여행가자/혜진.py)
```py
```

</div>
</details>
