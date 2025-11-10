"""
사람들 연속도니 번호
첫 째줄 -> n
둘 째주 -> 촌 수 계산 번호
셋 째줄 : 부모 자식 간의 관계의 수
넷째 줄 :부모 자식간의 관계 x,y x는 y의 부모

관계가 없으면 -1

graph dict에 노드와 연결된 놈들을 리스트로 저장해주기
큐를 이용하여 탐새갛면서 찾기 
빈 큐가 되면 종료
"""

from collections import deque

N = int(input())
start,finish = map(int,input().split())
M = int(input())
graphs = {}

for _ in range(M):
    x,y = map(int,input().split())
    if x not in graphs :
        graphs[x] = [y]
    else :
        graphs[x].append(y)
    if y not in graphs :
        graphs[y] = [x]
    else :
        graphs[y].append(x)
visited = set()
q = deque()
q.append((start,0))
visited.add(start)
result = 0

while q :
    x,chon = q.pop()
    visited.add(x)
    if finish in graphs[x] : #목적지가 여기 있나?
        print(chon+1)
        exit()
    for node in graphs[x]:
        if node not in visited :
            q.append((node,chon+1))
print(-1)