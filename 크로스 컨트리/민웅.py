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