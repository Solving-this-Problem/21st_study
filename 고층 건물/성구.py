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
