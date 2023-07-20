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
