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
```
## [서희](./크로스%20컨트리/서희.py)
```py
```
## [성구](./크로스%20컨트리/성구.py)
```py
# 9017 크로스 컨드티
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
```
## [서희](./쉬운%20최단거리/서희.py)
```py
```
## [성구](./쉬운%20최단거리/성구.py)
```py
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
```
## [서희](./고층건물/서희.py)
```py
```
## [성구](./고층건물/성구.py)
```py
```
## [혜진](./여행가자/혜진.py)
```py
```

</div>
</details>
