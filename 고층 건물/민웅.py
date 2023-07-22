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