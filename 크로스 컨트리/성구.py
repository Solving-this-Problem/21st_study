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
                
            
    
