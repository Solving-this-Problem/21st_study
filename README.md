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
