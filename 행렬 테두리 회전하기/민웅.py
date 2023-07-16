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